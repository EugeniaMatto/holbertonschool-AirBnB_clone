#!/usr/bin/python3
""""
module with class filestorage
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
<<<<<<< HEAD
=======
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
>>>>>>> ema

class FileStorage():
    """
    define class filestorage
    """
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """return objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """sets in objects"""
        FileStorage.__objects[str(obj.__class__.__name__) + '.' + str(obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """ deserializes the JSON file to """
        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, "r") as f:
                obj = json.load(f)
            self.__objects = {}
            for key, value in obj.items():
<<<<<<< HEAD
                """value = eval(value["__class__"])(**value)"""
                clas = value["__class__"]
                self.__objects[key] = eval(clas)(value)
=======
                 self.__objects[key] = eval(value["__class__"])(**value)
>>>>>>> ema

    def delete(self, key):
        """ delete objects"""
        FileStorage.__objects.pop(key)

    @staticmethod
    def all_class():
        return ["BaseModel", "User", "City", "Amenity", "Review", "Place", "State"]

    @staticmethod
    def set_atr(k , dic):
        try:    
            FileStorage.__objects[k].sett_atr(dic)
        except Exception:
            print("** no instance found **")
