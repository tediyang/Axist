#!/usr/bin/python3
""" This is the model that all other Class Object will inherits from.

    Description:
    1. This model consists of two class attributes which are:
      - id: A unique primary key for each object generated. 
      - created_at: datetime of object created
      - updated_at: datetime when data is updated.
    
    2. It will provide the following public instance methods:
      - save: save any object generated to the storage.
      - delete: delete object from the storage.
      - to_dict: generate a dictionary format of the object attributes.
"""

from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid


class BaseModel:
    """ All other classes will inherit from this class."""
    def __init__(self, *args, **kwargs):
        """Initialization"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        #loop through the keyword args and set the attributes
        for key, value in kwargs.items():
            if key == 'type()':
                continue
            setattr(self, key, value)
            if type(self.created_at) is str: #check if its a string data type
                self.created = datetime.fromisoformat(value)
            if type(self.updated_at) is str:
                self.updated_at = self.created_at
    
    def __str__(self):
        """How BaseModel should be represented in string"""
        return f("[{type(self).__name__}] ({self.id}) {self.dict}")

    def save(self):
        """ a function that updates the attribute with the current datetime an save in db"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """A function to delete object saved in storage"""
        models.storage.delete(self)

    def to_dict(self):
        """Returns a dictionary of the object class"""
        #set and empty dictionary
        New_dict = {}
        New_dict["type()"] = type(self).__name__
        #Loop throught the dict
        for key, value in vars(self).items():
            if key == "_sa_instance_state":
                pass
            elif isinstance(value, datetime.datetime):
                New_dict[key] = value.isoformat()
            else:
                New_dict[key] = value
        return New_dic
