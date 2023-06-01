#!/usr/bin/python3
"""
    Test module for User model, checking for expected behavoir
    and documentation.
"""

import inspect
from models import user
from models.base_model import BaseModel
import pycodestyle
import unittest

User = user.User


class TestUserDocs(unittest.TestCase):
    """Tests to check the documentation and style of User class"""

    @classmethod
    def setUpClass(cls):
        """
           Set up for the docstring tests by extracting all the function
           object.
        """
        cls.user_f = inspect.getmembers(User, inspect.isfunction)

    def test_pep8_conformance(self):
        """Test that models/user.py conforms to PEP8 (pycodestyle)."""
        for path in ['models/user.py',
                     'test_user.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_user_module_docstring(self):
        """Test for the user.py module docstring"""
        self.assertIsNot(user.__doc__, None,
                         "user.py needs a docstring")
        self.assertTrue(len(user.__doc__) >= 1,
                        "user.py needs a docstring")

    def test_user_class_docstring(self):
        """Test for the User class docstring"""
        self.assertIsNot(User.__doc__, None,
                         "User class needs a docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class needs a docstring")

    def test_user_func_docstrings(self):
        """Test for the presence of docstrings in User methods"""
        for func in self.user_f:
            with self.subTest(func=func):
                self.assertIsNot(func[1].__doc__, None,
                                 "{:s} method needs a docstring".
                                 format(func[0]))
                self.assertTrue(len(func[1].__doc__) >= 1,
                                "{:s} method needs a docstring".
                                format(func[0]))


class TestUser(unittest.TestCase):
    """Test the User class"""
    def test_is_subclass(self):
        """Test that User is a subclass of BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_email_attr(self):
        """
           Test that User has attr email, and contains @ in it.
        """
        user = User()
        user.email = "abcdefgh@xyz.com"
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "abcdefgh@xyz.com")
        self.assertIn('@', user.email)

    def test_password_attr(self):
        """
           Test that User has attr password, and the value
           is encoded.
        """
        user = User()
        user.password = "Axistuser123#"
        self.assertTrue(hasattr(user, "password"))
        self.assertNotEqual(user.password, "Axistuser123#")

        # Hashlib md5 is represented as 32 hexadecimal digits
        self.assertEqual(len(user.password), 32)

    def test_first_name_attr(self):
        """ Test that User has attr first_name only if provided. """
        user = User()
        if "first_name" in user.__dict__:
            self.assertNotEqual(user.first_name, None)

    def test_last_name_attr(self):
        """Test that User has attr last_name only if provided. """
        user = User()
        if "last_name" in user.__dict__:
            self.assertNotEqual(user.last_name, None)

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary with proper attrs"""
        u = User()
        u.password = "Chichi"
        new_d = u.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in u.__dict__:
            if attr == "password":  # confirm password is not displayed.
                self.assertFalse(attr in new_d)
                break
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """Test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = User()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "User")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))


if __name__ == "__main__":
    unittest.main()
