#!/usr/bin/python3
""" Task module """
import uuid
from datetime import datetime
from datetime import timezone


class Task:
    __no_of_tasks = 0
    
    def __init__(self, description, status, created_at, updatedAt):
        self.id = str(uuid.uuid4())
        self.description = description
        self.status = status or "not done"
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at
        
        self.__no_of_tasks += 1
