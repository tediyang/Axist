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
    ID = ""
    password = ""
    

    def __init__(self, username, password):
        """ initilization """
        self.username = username
        self.ID = self.generate_ID()
        

    @staticmethod
    def generate_ID():
        """Generate unique id"""
        return str(uuid.uuid(4))

    @staticmethod
    def encrypt_password(password):
        """ Generates the password in a secured manner
            using salt() and convert to bytes using encode()
            and converts hashed pswd to string
        """
        salt = bcrypt.gensalt() 
        password_bytes = password.encode('utf-8') 
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        return hashed_password.decode('utf-8')

    def check_password(self, password):
        """
            converts passwd to bytes, hashed passwd to bytes
            and compares the hashed to see if it matches
        """
        password_bytes = password.encode('utf-8')
        hashed_password = self.password.encode('utf-8')
        return bcrypt.checkpw(password_bytes, hashed_password)

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = self.encrypt_password(password)

user = User("mawoda2")
password = input("Enter password: ")
user.set_password(password)
print(user.id)
print(user.get_password())
