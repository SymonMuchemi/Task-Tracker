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
        self.id = self.__no_of_tasks
        self.status = "not done"
        self.description = description
        self.created_at = str(datetime.now(timezone.utc))
        self.updated_at = self.created_at

        for key, val in kwargs.items():
            if key == "description":
                self.description = val
            if key == "status":
                self.status = val
            if key == "created_at" and val is not None:
                self.created_at = val
            if key == "updated_at" and val is not None:
                self.updated_at = val

    def update(self, *args, **kwargs):
        """updates the instance atttibutes
        """
        for key, val in kwargs.items():
            if key == "description":
                self.description = val
            if key == "status":
                self.status = val
            if key in ["created_at", "updated_at"] and val is not None:
                val = datetime.strptime(val, time_format)
                setattr(self, key, val.strftime(time_format))
            self.updated_at = datetime.now(timezone.utc).strftime(time_format)

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
        """creates a Task object from a dictionary

        Args:
            data (dict): the data dictionary

        Returns:
            Task: new task object
        """
        return cls(
            description=data.get('description', ''),
            status=data.get('status', ''),
            created_at=data.get('created_at'),
            updated_at=data.get('updated_at')
        )

    def __str__(self) -> str:
        return f"[{self.id}] {self.description} ({self.status})"
