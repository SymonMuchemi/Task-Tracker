#!/usr/bin/python3
""" Task module """
from datetime import datetime
from datetime import timezone

time_format = "%Y-%m-%dT%H:%M:%S"



class Task:
    __no_of_tasks = 0
    
    def __init__(self, description, *args, **kwargs):
        """ Initializes a Task object """
        Task.__no_of_tasks += 1
        if kwargs:
            for key, val in kwargs.items():
                if key == "description":
                    self.description = val
                if key == "status":
                    self.status = val
                if key == "created_at" and val is not None:
                    self.created_at = datetime.strptime(val, time_format)
                if key == "updated_at" and val is not None:
                    self.created_at = datetime.strptime(val, time_format)
        else:
            self.id = self.__no_of_tasks
            self.status = "not done"
            self.description = description
            self.created_at = str(datetime.now(timezone.utc))
            self.updated_at = self.created_at
        

    def update(self, *args, **kwargs):
        """updates the instance atttibutes
        """
        if not kwargs:
            if len(args) > 0 and args[0] is not None:
                self.id = args[0]
            if args[1] is not None and isinstance(args[1], str):
                self.description = args[1]
            if args[2] is not None and isinstance(args[2], str):
                self.status = args[2]
            if args[3] is not None and isinstance(args[3], datetime):
                self.created_at = args[3]
            if args[4] is not None and isinstance(args[4], datetime):
                self.created_at = args[4]
        else:
            for key, val in kwargs.items():
                if key == "updated_at" or "created_at":
                    val = datetime.strptime(kwargs["updated_at"],
                                            '%Y-%m-%dT%H:%M:%S.%f')
                    val = str(val)
                if key == "description":
                    self.description = val
                if key == "id":
                    self.id = val
                if key == "status":
                    self.status = val

    def to_dict(self):
        """returns a dictionary version of the instance
        with the description as key

        Returns:
            dict: dictionary version of the instance
        """
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @classmethod
    def from_dict(cls, data):
        # print(data.items()) # TODO: remove debug line
        return cls(
            id=data.get('id', None),
            description=data.get('description', ''),
            status=data.get('status', ''),
            created_at=data.get('created_at', None),
            updated_at=data.get('updated_at', None)
        )
