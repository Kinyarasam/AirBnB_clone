#!/usr/bin/python3
"""Test Review"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.user import User


class Testreview(unittest.TestCase):
    """unit test"""
    def test_class(self):
        rev1 = Review()
        self.assertEqual(rev1.__class__.__name__, "Review")

    def test_father(self):
        rev1 = Review()
        self.assertTrue(issubclass(rev1.__class__, BaseModel))

    def test_review(self):
        """
        Test review
        """
        my_review = Review()
        self.assertTrue(hasattr(my_review, "place_id"))
        self.assertEqual(my_review.place_id, "")
        self.assertTrue(hasattr(my_review, "user_id"))
        self.assertEqual(my_review.user_id, "")
        self.assertTrue(hasattr(my_review, "text"))
        self.assertEqual(my_review.text, "")

    def setUp(self):
        self.review = Review()
        self.attr_list = [
            "place_id",
            "user_id",
            "text"
        ]

    def test_review_is_a_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.review), BaseModel))

    def test_attrs_are_class_attrs(self):
        for attr in self.attr_list:
            self.assertTrue(hasattr(self.review, attr))

    def test_class_attrs(self):
        for attr in self.attr_list:
            self.assertIs(type(getattr(self.review, attr)), str)
            self.assertFalse(bool(getattr(self.review, attr)))


if __name__ == "__main__":
    unittest.main()
