#!/usr/bin/python3
"""
    Test module for Location model, checking for expected behavoir
    and documentation.
"""

import inspect
from models import geolocation
from models.base_model import BaseModel
from models.user import User
import pycodestyle
import unittest

Location = geolocation.Location


class TestLocationDocs(unittest.TestCase):
    """Tests to check the documentation and style of Location class"""

    @classmethod
    def setUpClass(cls):
        """
           Set up for the docstring tests by extracting all the function
           object.
        """
        cls.geolocation_f = inspect.getmembers(Location, inspect.isfunction)

    def test_pep8_conformance(self):
        """Test that models/geolocation.py conforms to PEP8 (pycodestyle)."""
        for path in ['models/geolocation.py',
                     'test_geolocation.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_geolocation_module_docstring(self):
        """Test for the geolocation.py module docstring"""
        self.assertIsNot(geolocation.__doc__, None,
                         "geolocation.py needs a docstring")
        self.assertTrue(len(geolocation.__doc__) >= 1,
                        "geolocation.py needs a docstring")

    def test_geolocation_class_docstring(self):
        """Test for the Location class docstring"""
        self.assertIsNot(Location.__doc__, None,
                         "Location class needs a docstring")
        self.assertTrue(len(Location.__doc__) >= 1,
                        "Location class needs a docstring")

    def test_geolocation_func_docstrings(self):
        """Test for the presence of docstrings in Location methods"""
        for func in self.geolocation_f:
            with self.subTest(func=func):
                self.assertIsNot(func[1].__doc__, None,
                                 "{:s} method needs a docstring".
                                 format(func[0]))
                self.assertTrue(len(func[1].__doc__) >= 1,
                                "{:s} method needs a docstring".
                                format(func[0]))


class TestLocation(unittest.TestCase):
    """Test the Location class"""
    def test_is_subclass(self):
        """Test that Location is a subclass of BaseModel"""
        location = Location()
        self.assertIsInstance(location, BaseModel)
        self.assertTrue(hasattr(location, "id"))
        self.assertTrue(hasattr(location, "created_at"))
        self.assertTrue(hasattr(location, "updated_at"))

    def test_latitude_longitude_attr(self):
        """
           Test that Location has attributes latitude and latitude.
        """
        location = Location()
        location.latitude = "37.38605"
        location.longitude = "-122.08385"
        self.assertTrue(hasattr(location, "longitude"))
        self.assertTrue(hasattr(location, "latitude"))
        self.assertEqual(type(location.latitude), str)
        self.assertEqual(type(location.longitude), str)

    def test_user_id_attr(self):
        """
           Test that Location has attr user_id.
        """
        location = Location()
        user = User()
        location.user_id = user.id
        self.assertRegex(location.user_id,
                         '^[0-9a-f]{8}-[0-9a-f]{4}'
                         '-[0-9a-f]{4}-[0-9a-f]{4}'
                         '-[0-9a-f]{12}$')

    def test_loc_name_attr(self):
        """ Test that Location has attr loc_name. """
        location = Location()
        location.loc_name = 'Home'
        self.assertEqual(location.loc_name, 'Home')

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary with proper attrs"""
        loc = Location()
        new_d = loc.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in loc.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """Test that values in dict returned from to_dict are correct."""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        lo = Location()
        new_d = lo.to_dict()
        self.assertEqual(new_d["__class__"], "Location")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], lo.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], lo.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        loc = Location()
        string = "[Location] ({}) {}".format(loc.id, loc.__dict__)
        self.assertEqual(string, str(loc))


if __name__ == "__main__":
    unittest.main()
