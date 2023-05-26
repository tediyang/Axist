#!/usr/bin/python3
"""
    This model inherits from the BaseModel and
    contains the locations of the user.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Location(BaseModel, Base):
	""" Representation of a location data. """
	__tablename__ = 'locations'
	latitude = Column(String(64), unique=True, nullable=False)
	longitude = Column(String(64), nullable=False)
	loc_name = Column(String(64), nullable=False)
	user_id = Column(String(64), ForeignKey('users.id'), nullable=False)

	def __init__(self):
		""" Initializes location """
		super().__init__()
