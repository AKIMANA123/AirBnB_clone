#!/usr/bin/python3
"""This module defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (__file_path)."""
        serialized_objs = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objs[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(serialized_objs, f)

    def reload(self):
        """Deserialize the JSON file to __objects if it exists."""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for key, val in obj_dict.items():
                    class_name = val["__class__"]
                    self.__objects[key] = eval(class_name)(**val)
        except FileNotFoundError:
            pass
