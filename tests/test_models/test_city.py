#!/usr/bin/python3
"""Test City"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.user import User


class Testcity(unittest.TestCase):
    """unit test"""
    def test_class(self):
        city1 = City()
        self.assertEqual(city1.__class__.__name__, "City")

    def test_dict_value(self):
        """
            test dict values
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        city = City()
        dict_con = city.to_dict()
        self.assertEqual(dict_con["__class__"], "City")
        self.assertEqual(type(dict_con["created_at"]), str)
        self.assertEqual(type(dict_con["updated_at"]), str)
        self.assertEqual(
                            dict_con["created_at"],
                            city.created_at.strftime(time_format)
                                        )
        self.assertEqual(
                            dict_con["updated_at"],
                            city.updated_at.strftime(time_format))

    def test_base(self):
        city1 = City()
        self.assertTrue(issubclass(city1.__class__, BaseModel))

    def test_city(self):
        """
        Test attributes of Class City
        """
        my_city = City()
        self.assertTrue(hasattr(my_city, "name"))
        self.assertEqual(my_city.name, "")
        self.assertTrue(hasattr(my_city, "state_id"))
        self.assertEqual(my_city.state_id, "")

    def setUp(self):
        self.city = City()
        self.attr_list = ["state_id", "name"]

    def test_city_is_a_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def test_attrs_are_class_attrs(self):
        for attr in self.attr_list:
            self.assertIs(type(getattr(self.city, attr)), str)
            self.assertFalse(bool(getattr(self.city, attr)))


if __name__ == "__main__":
    unittest.main()
