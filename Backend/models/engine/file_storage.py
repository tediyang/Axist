#!/usr/bin/python3
"""
    This is filestorage class
"""
import json
from models.basemodel import BaseModel

# Dictionary of class objects
classes = {"BaseModel": BaseModel, "Geolocation": Geolocation, "User": User}

class FileStorage:
    """It does the magic. converting objects to json and json to object"""
    #Private Attributes
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """ return {} of __objects """
        #check if its a class or None
        if cls = None:
            return FileStorage.__objects

        #create a dummy dict. set if empty
        dummy = {}
        #loop thro and check for key
        for key, value in FileStorage.__objects.items():
            if cls.__name__ in key:
                dummy[key] = value
            return dummy

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        if obj != None:
            key = f("{obj.__class__.__name__}.{obj.id}")
            value = obj
            FileStorage.__object[key] = value

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        #initialize the json_objects dict
        json_objects = {}
        #loop thro the __objects
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
            #write into the file
            with open(self.__file_path, 'w') as f:
                json.dump(json_objects, f)




