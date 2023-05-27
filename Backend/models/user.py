#!/usr/bin/python3
"""
    This model inherits from the BaseModel and
    contains the user data.
"""

from base_model import BaseModel, Base
from sqlalchemy import Column, String
from hashlib import md5
import secrets

class User(BaseModel, Base):
    """ Representation of a user data. """
    __tablename__ = 'users'
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(64), nullable=False)
    password_reset_token = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False)
    first_name = Column(String(64), nullable=True)
    last_name = Column(String(64), nullable=True)

    def __init__(self):
        """initializes user"""
        super().__init__()

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)

    def generate_password_reset_token(self):
        """ we make a unique token that is sent to user email to reset password """
        token = secrets.token_hex(16)
        self.password_reset_token = token

    def reset_password(self, new_password):
        """ reset the password to the new one """
        self.password = new_password
        self.reset_token = None

    def password_to_email(self):
        pass