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
    pass