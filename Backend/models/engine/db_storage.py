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
"""

from models.base_model import Base
import models
from models.geolocation import Location
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


classes = {"User": User, "Location": Location}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        AXIST_MYSQL_USER = "axist_user"
        AXIST_MYSQL_PWD = "Axistuser123#"
        AXIST_MYSQL_HOST = "localhost"
        AXIST_MYSQL_DB = "axist"
        AXIST_ENV = "db"

        self.__engine = create_engine('mysql+mysqlconnector://{}:{}@{}/{}'.
                format(AXIST_MYSQL_USER,
                    AXIST_MYSQL_PWD,
                    AXIST_MYSQL_HOST,
                    AXIST_MYSQL_DB))

                #if AXIST_ENV == "test":
                #    Base.metadata.drop_all(self.__engine)

    def all(self, cls):
        """
            query on the current database session and return all
            data based on the provided cls.
        """
        new_dict = {}
        for clss in classes:
            if cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)        

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def update(self, cls, id, dic):
        """
            update the user's data.

            cls: Object
            id: unique id of Object (string)
            dic: data of key-value pairs to be updated 
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)

        if cls == classes["User"]:
            # Using filter and lambda func to get user_data.
            user_data = filter(lambda x: x.id == id, all_cls.values())
            if user_data[0]:
                for key, value in dic.items():
                    setattr(user_data[0], key, value)

        models.storage.save()

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session


    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
