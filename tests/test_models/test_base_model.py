"""
Unit Testing for BaseModel class
"""
from models import BaseModel
from datetime import datetime
import models
import time
import unittest


class TestBaseModel(unittest.TestCase):
    """ Testing the Base Class """
    def test_doc1(self):
        """ test documentation for module """
        res = "Module has no documentation"
        self.assertIsNotNone(models.base_model.__doc__, res)

    def test_doc2(self):
        """test documentation for class """
        res = "Module has no documentation"
        self.assertIsNotNone(models.base_model.BaseModel.__doc__, res)

    def test_doc3(self):
        """testing for methods"""
        res = "method init has no documentation"
        self.assertIsNotNone(models.base_model.BaseModel.__init__.__doc__, res)
        res1 = "method __str__ has no documentation"
        self.assertIsNotNone(models.base_model.BaseModel.__str__.__doc__, res1)
        res2 = "method save has no documentation"
        self.assertIsNotNone(models.base_model.BaseModel.save.__doc__, res2)
        res3 = "method to_dict has no documentation"
        self.assertIsNotNone(models.base_model.BaseModel.to_dict.__doc__, res3)

    def test_str(self):
        """ test str method """
        instance = BaseModel()
        correct_str = "[BaseModel] ({}) {}".format(
                instance.id, instance.__dict__
            )
        self.assertEqual(correct_str, str(instance))

    def to_dict_value(self):
        """ test return value of dict """
        ti = "%Y-%m-%dT%H:%M:%S.%f"
        inst = BaseModel()
        dict_base = instance.to_dict()
        self.assertEqual(dict_base["__class__"], "BaseModel")
