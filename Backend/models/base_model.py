#!/usr/bin/python3
""" This is the model that all other Class Object will inherits from.

    Description:
    1. This model consists of three class attributes which are:
      - id: A unique primary key for each object generated. 
      - created_at: datetime of object created
      - updated_at: datetime when data is updated.

    2. It will provide only one public instance attribute 'id',
    where the unique id will be defined with uuid4.

    3. It will provide the following public instance methods:
      - save: save any object generated to the storage.
      - delete: delete object from the storage.
      - to_dict: generate a dictionary format of the object attributes.
"""

from datetime import datetime
from models import storage
from sqlalchemy import Column, String, DateTime
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
import uuid


time = "%Y-%m-%dT%H:%M:%S.%f"
Base = declarative_base()


class BaseModel:
    """ All other models will inherit from this BaseModel. """

    # Class attributes which other models will inherit.
    id = Column(String(60), primary_key=True)

    # Generate default values in the database.
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
  
    def __init__(self):
        """ initialization of the id instance """
        self.id = str(uuid.uuid4())

    def __str__(self):
        """ string representation of the Object class """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the attribute 'updated_at' with the current datetime """
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
            new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        if "password" in new_dict:
            del new_dict["password"]

        return new_dict

    def delete(self):
        """ deletes the current object saved in storage """
        storage.delete(self)