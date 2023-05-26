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
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid


Base = declarative_base()


class BaseModel:
  """ All other models will inherit from this BaseModel."""

  # Class attributes which other models will inherit.
  id = Column(String(60), primary_key=True)
  created_at = Column(DateTime, default=datetime.utcnow)
  updated_at = Column(DateTime, default=datetime.utcnow)
  
  def __init__(self):
    """ initialization of the id instance """
    self.id = str(uuid.uuid4())

  def __str__(self):
    """ string representation of the Object class """
    return f"[{self.__class__.__name__}] ({self.id}) {self.dict}"

  def save(self):
    """ updates the attribute 'updated_at' with the current datetime """
    self.updated_at = datetime.utcnow()

  def delete(self):
    """ deletes the current object saved in storage """
    pass
