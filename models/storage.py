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
            File_storage.__objects.all().update(
                {
                    obj.to_dict()['description']: obj
                }
            )

    def save(self):
        """save storage to file"""
        with open(self.__file_path, "w") as file:
            temp_dict = {}
            temp_dict.update(File_storage.__objects)
            for key, val in temp_dict:
                temp_dict[key] = val.to_dict()
            json.dump(temp_dict)
            
