#!/usr/bin/python3
""" __init__ modules """
from .base_model import BaseModel
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()