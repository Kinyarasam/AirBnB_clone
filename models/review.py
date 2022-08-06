#!/usr/bin/python3
"""class Review that inherits from class BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines the Review class
    """
    place_id = ""
    user_id = ""
    text = ""
