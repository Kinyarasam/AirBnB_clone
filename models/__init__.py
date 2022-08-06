#!/usr/bin/python3
""" __init__ modules """
from models.engine.file_storage import FileStorage
from .base_model import BaseModel
from .user import User
from .city import City
from .state import State
from .amenity import Amenity
from .place import Place

storage = FileStorage()
storage.reload()
