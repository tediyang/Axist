""" importing all the needed modules """
import uuid # unique user id generation
import bcrypt # to encrypt the password
class User:
    """
        Attributes and methods of the class are defined here
    """
    # class variables
    username = ""
    user_id = ""
    password = ""
    def __init__(self, username, user_id, password):
        """ initilization """
        self.username = username
        self.user_id = self.generate_user_id()
        self.password = self.encrypt_password(password)

    @staticmethod
    def encrypt_password(password):
        """ Generates the password in a secured manner """
        salt = bcrypt.gensalt() #generates salt for hashing
        password_bytes = password.encode('utf-8') # convert password to bytes
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        return hashed_password.decode('utf-8')

    def check_password(self, password):
        password_bytes = password.encode('utf-8')
        return bcrypt.checkpw(password_bytes, hasted_password)
