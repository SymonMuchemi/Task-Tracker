#!/usr/bin/python3
""" storage module """
import json
from task import Task


class File_storage:
    __file_path = 'tasks.json'
    __objects = {}
    
    def all(self, id=None):  
        """returns all the objects stored in the objects dictionary

        Returns:
            dict: dictionary of objects
        """
        if id is not None:
            return {
                key: val for key, val in File_storage.__objects.items() if key == int(id)
            }
        return self.__objects

    def new(self, obj):
        """adds a new object to the objects dict

        Args:
            obj (dict): object to be added
        """
        if obj is not None:
            key = obj.id
            self.__objects[key] = obj

    def load(self):
        """Loads storage from file"""
        with open(File_storage.__file_path, 'r') as file:
            temp_dict = json.load(file)
            for key, val in temp_dict.items():
                File_storage.__objects[key] = Task.from_dict(val)
    
    def save(self):
        """save storage to file"""
        objects = {}
        for key in self.__objects:
            objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w+') as file:
            json.dump(objects, file)

    def reload(self):
        """deserializes data from the json file"""
        try:
            with open(File_storage.__file_path, 'r') as file:
                objects = json.load(file)
            for key, val in objects.items():
                class_name = val['__class__']
                obj = eval(class_name)(**val)
                self.__objects[key] = obj
        except:
            pass

    def close(self):
        """calls the reload method"""
        self.reload()
