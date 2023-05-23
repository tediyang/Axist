#!/usr/bin/python3

""" importing all the needed modules """
import uuid # unique user id generation
import bcrypt # to encrypt the password
class User:
    """
        Attributes and methods of the class are defined here
    """
    # class variables
    username = ""
    id = ""
    password = ""
    

    def __init__(self, username, user_id, password):
        """ initilization """
        self.username = username
        self.id = self.generate_id()
        self.password = self.encrypt_password(password)

    @staticmethod
    def generate_id():
        "Generate unique id"
        return str(uuid.uuid(4))

    @staticmethod
    def encrypt_password(password):
        """ Generates the password in a secured manner
            using salt() and convert to bytes using encode()
        """
        salt = bcrypt.gensalt() 
        password_bytes = password.encode('utf-8') 
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        return hashed_password.decode('utf-8')

    def check_password(self, password):
        password_bytes = password.encode('utf-8')
        return bcrypt.checkpw(password_bytes, hashed_password)
