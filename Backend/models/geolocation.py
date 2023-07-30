#!/usr/bin/python3
"""
    This model inherits from the BaseModel and
    contains the locations of the user.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
# from sqlalchemy.orm import relationship


class Location(BaseModel, Base):
    """ Representation of a location data. """
    __tablename__ = 'locations'
    user_id = Column(String(64), ForeignKey('users.id'), nullable=False)
    latitude = Column(String(64), nullable=False)
    longitude = Column(String(64), nullable=False)
    saved_name = Column(String(64), nullable=False)

    def __init__(self, *args, **kwargs):
        """ Initializes location """
        super().__init__(*args, **kwargs)
