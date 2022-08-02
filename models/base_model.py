#!/usr/bin/python3
""" Defines a BaseModel Class """
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ Represents the BaseModel

    Attributes:
        __nb_objects (int): The number of instantiated Bases

    """
    def __init__(self, *args, **kwargs):
        """ Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()
        else:
            BaseModel.__nb_objects += 1
            self.id = BaseModel.__nb_objects

    def save(self):
        """ Updates the public instance attribute """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values """
        temp = dict(self.__dict__)
        temp['__class__'] = self.__class__.__name__
        temp['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        temp['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return temp
