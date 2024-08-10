#!/usr/bin/python3
""" storage module """
import json


class File_storage:
    __file_path = 'tasks.json'
    __objects = {}
    
    def all(self):  
        """returns all the objects stored in the objects dictionary

        Returns:
            dict: dictionary of objects
        """
        return {
            key: val for key, val in File_storage.__objects.items()
        }

    def new(self, obj):
        """adds a new object to the objects dict

        Args:
            obj (dict): object to be added
        """
        if obj is not None:
            key = obj.description
            self.__objects[key] = obj

    def save(self):
        """save storage to file"""
        objects = {}
        for key in self.__objects:
            objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(objects, file)
