#!/usr/bin/python3
"""
    This is a DataBase Storage using MySQL

    Description:
    1. This DB consists of two private class attributes
    2. The storage public instance methods include:
      - all: fetch all the data from a specific table.
      - new: add new object to the storage.
      - save: commit new changes to the storage.
      - delete: delete object from the storage.
      - update: update to data in the storage.
      - reload: setup the storage session.
      - close: remove the session.
    First import neccessary modules.
"""

from models.base_model import Base
from models.user import User
from models.geolocation import Location
from os import getenv
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from  typing import Dict, Type, Optional, Any


# handle environmental files. This part is not neccessary 
#since we are already using getenv method. dont need to load path.
path = find_dotenv("axist.env")
load_dotenv(path)

classes: Dict[str, type] = {"User": User, "Location": Location}


class DBStorage:
    """interacts with the MySQL database"""
    __engine: Any = None
    __session: Any = None

    def __init__(self) -> None:
        """Instantiate a DBStorage object"""
        user: str | None = getenv('AXIST_MYSQL_USER')
        pwd : str | None = getenv('AXIST_MYSQL_PWD')
        host: str | None = getenv('AXIST_MYSQL_HOST')
        db: str | None = getenv('AXIST_MYSQL_DB')

        #  set engine privately
        self.__engine = create_engine(f'mysql+mysqlconnector://{user}:{pwd}@{host}/{db}')

        if getenv('AXIST_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls: Type[User] | Type[Location]) -> Dict:
        """
            query on the current database session and return all
            data based on the provided cls.
        """
        # initialize the dict
        new_dict: Dict[str, Type] = {}
        # iterate of the items in classes and check for conditions
        for clss in classes:
            if cls == classes[clss] or cls == clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj: Type[User] | Type[Location]) -> None:
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self) -> None:
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj: Optional[User] | Optional[Location] = None) -> None:
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)
            self.__session.commit()

    def update(self, cls: type, id: str, dic: Dict[str, Any]) -> None:
        """
            update the user's data.

            cls: Object
            id: unique id of Object (string)
            dic: data of key-value pairs to be updated
        """
        if cls not in classes.values():
            return None

        obj = self.get(cls, id)

        if obj:
            for key, value in dic.items():
                setattr(obj, key, value)
            obj.save()
            self.save()

    def get(self, cls: Type, id: str) -> Optional[Any]:
        """A method to retrieve one object"""
        if cls and id:
            data = self.all(cls)
            search = "{}.{}".format(cls.__name__, id)
            if search in data.keys():
                return data[search]

        return None

    def reload(self) -> None:
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self) -> None:
        """call remove() method on the private session attribute"""
        self.__session.remove()
