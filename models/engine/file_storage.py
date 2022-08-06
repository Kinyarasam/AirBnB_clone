"""
FileStorage that serializes and deserializes instances to a JSON file
"""
import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """ String represemting a simple data structure in JSON format.
        example: '{ "12": { "numbers": [1, 2, 3], "name": "John" } }'
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        dict_key = obj.__class__.__name__ + '.' + obj.id
        self.__objects.update({dict_key: obj})

    def save(self):
        """ Serialises __objests to the JSON file """
        dict = {}
        for key in self.__objects:
            dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(dict, f, sort_keys=True, indent=4)
            # json.dump(dict, f, sort_keys=True)
            # json.dump(dict, f)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                json_obj = json.load(f)
                for key, val in json_obj.items():
                    self.__objects[key] = eval(val["__class__"])(**val)
