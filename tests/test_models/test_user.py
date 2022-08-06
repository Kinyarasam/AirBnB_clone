#!/usr/bin/python3
"""Test User
"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """unit test
    """
    def test_User(self):
        """Test use of Class
        """
        my_user = User()
        self.assertTrue(hasattr(my_user, "first_name"))
        self.assertEqual(my_user.first_name, "")
        self.assertTrue(hasattr(my_user, "last_name"))
        self.assertEqual(my_user.last_name, "")
        self.assertTrue(hasattr(my_user, "email"))
        self.assertEqual(my_user.email, "")
        self.assertTrue(hasattr(my_user, "password"))
        self.assertEqual(my_user.password, "")

    def test_attrs_are_class_attrs(self):
        """testing the class attrs
        """
        u = User()
        self.assertTrue(hasattr(
            User, "first_name"
        )) and hasattr(
            User, "last_name"
        )

    def test_class_attrs(self):
        u = User()
        self.assertIs(type(u.first_name), str)
        self.assertIs(type(u.last_name), str)
        self.assertTrue(u.first_name == "")
        self.assertTrue(u.last_name == "")

    def test_subclass(self):
        """Test User is a BaseModel subclass
        """
        u = User()
        self.assertTrue(issubclass(type(u), BaseModel))


if __name__ == "__main__":
    unittest.main()
