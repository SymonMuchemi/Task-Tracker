#!/usr/bin/python3
""" Task module """
import uuid
from datetime import datetime
from datetime import timezone


class Task:
    __no_of_tasks = 0
    
    def __init__(self, description, status="not done"):
        """
        Initializes a Task object.
        Parameters:
        - description (str): The description of the task.
        - status (str, optional): The status of the task. Defaults to "not done".
        Attributes:
        - status (str): The status of the task.
        - id (str): The unique identifier of the task.
        - description (str): The description of the task.
        - created_at (datetime): The date and time when the task was created.
        - updated_at (datetime): The date and time when the task was last updated.
        """
        self.status = status
        self.id = str(uuid.uuid4())
        self.description = description
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at
        
        self.__no_of_tasks += 1

    def update(self, *args, **kwargs):
        
