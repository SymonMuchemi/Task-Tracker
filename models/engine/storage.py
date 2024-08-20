#!/usr/bin/python3
""" storage module """
import json
from ..task import Task


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
        try:
            with open(File_storage.__file_path, 'r') as file:
                temp_dict = json.load(file)
                for key, val in temp_dict.items():
                    File_storage.__objects[int(key)] = Task.from_dict(val)
        except FileNotFoundError:
            pass
    
    def save(self):
        """save storage to file"""
        objs = {key: obj.to_dict() for key, obj in self.__objects.items()}
        
        with open(self.__file_path, 'w+') as file:
            json.dump(objs, file)

    def close(self):
        """calls the reload method"""
        self.reload()

    def delete(self, obj):
        """deletes obj from storage"""
        if obj is not None:
            key_to_del = None
            for key, val in self.__objects.items():
                if val == obj:
                    key_to_del = key
                    break
            if key_to_del is not None:
                del self.__objects[key_to_del]
                self.save()
