#!/usr/bin/python3
"""Class User that inherits from class BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class Defining a User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
