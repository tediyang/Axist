#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

import inspect
from models.engine import db_storage
from models.geolocation import Location
from models.user import User
import pycodestyle
import unittest

DBStorage = db_storage.DBStorage
storage = DBStorage()
classes = {"Location": Location, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance(self):
        """
           Test that models/engine/db_storage.py
           conforms to PEP8 (pycodestyle).
           """
        for path in ['models/engine/db_storage.py',
                     'test_db_storage.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestDBStorage(unittest.TestCase):
    """Test the DBStorage class"""
    def test_all(self):
        """
           Test that all returns all data based on the provided cls.
        """
        # start the session
        storage.reload()
        # create an instance to test
        instance = User()
        instance.email = "axist@axist.com"
        instance.username = "axist02"
        instance.password = "axist123#"
        storage.new(instance)
        storage.save()

        data = storage.all(User)
        self.assertGreater(len(data), 0)

    def test_new_save(self):
        """Test that save properly saves objects to db"""
        # start a session
        storage.reload()
        # fetch old data
        objs_old = storage.all(User)
        # create instance
        instance = User()
        instance.email = "axist@axist.com"
        instance.username = "axist03"
        instance.password = "axist123#"
        storage.new(instance)
        storage.save()

        # start new session to check if data was saved.
        storage.reload()
        # fetch new data
        objs_new = storage.all(User)

        self.assertNotEqual(len(objs_old), len(objs_new))

    def test_delete(self):
        """Test that delete properly remove the obj from the db"""
        # start a session
        storage.reload()
        # create instance
        instance = User()
        instance.email = "axist@axist.com"
        instance.username = "axist04"
        instance.password = "axist123#"
        storage.new(instance)
        storage.save()

        # before delete
        objs_old = storage.all(User)
        # delete
        storage.delete(instance)

        objs_new = storage.all(User)
        self.assertNotEqual(len(objs_old), len(objs_new))

    def test_get(self):
        """Test that get properly fetch the object"""
        # start a session
        storage.reload()
        # create an instance to test
        instance = User()
        instance.email = "axist@axist.com"
        instance.username = "axist05"
        instance.password = "axist123#"
        id = instance.id

        storage.new(instance)
        storage.save()

        get_obj = storage.get(User, id)

        self.assertEqual(id, get_obj.id)
        self.assertIsInstance(get_obj, User)
        self.assertEqual(type(id), str)

    def test_update(self):
        """Test that update made changes to the data"""
        # start a session
        storage.reload()
        # create a instance
        instance = User()
        instance.username = 'axist'
        instance.email = 'axist@axist.com'
        instance.password = 'Axist123##'
        id = instance.id
        storage.new(instance)
        storage.save()

        up_axist = {'username': 'AxistSuper',
                    'email': 'axist@gmail.com'}
        storage.update(User, id, up_axist)
        obj = storage.get(User, id)
        self.assertNotEqual(obj.username, 'axist')
        self.assertNotEqual(obj.email, 'axist@axist.com')


if __name__ == "__main__":
    unittest.main()
