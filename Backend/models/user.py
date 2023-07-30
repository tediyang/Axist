#!usr/bin/python3
"""
    This model inherits from the BaseModel and
    contains the user data.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from flask_bcrypt import generate_password_hash


class User(BaseModel, Base):
    """ Representation of a user data. """
    __tablename__ = 'users'
    email = Column(String(64), unique=True, nullable=False)
    password = Column(String(64), nullable=False)
    username = Column(String(64), unique=True)
    first_name = Column(String(64))
    last_name = Column(String(64))
    locations = relationship("Location", backref="user", cascade="all delete-orphan")

    def __init__(self, *args, **kwargs) -> None:
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name: str, value: str) -> None:
        """sets a password with md5 encryption"""
        if name == "password":
            value = generate_password_hash(value).decode('utf8')
        if name == 'username':
            value = value.lower().strip()
        super().__setattr__(name, value)
