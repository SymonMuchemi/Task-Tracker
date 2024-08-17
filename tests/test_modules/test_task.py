#!/usr/bin/python3
""" test the Task model """
import unittest
import os
from models.task import Task
from datetime import datetime


class TestTask(unittest.TestCase):
    __file_path = 'test_data.json'

    @classmethod
    def setUpClass(cls):
        cls.time_now = datetime.now()
        cls.new = Task("Check attributes", status="not done")


    def tearDown(self) -> None:
        """
        Clean up method that is called after each test case.
        Removes the file specified by the file path if it exists.
        """
        
        if os.path.isfile(TestTask.__file_path):
            os.remove(TestTask.__file_path)

    def test_attributes(self):
        """checks file attributes """
        
        self.assertIsNotNone(TestTask.new.id)
        self.assertIsNotNone(TestTask.new.status)
        self.assertIsNotNone(TestTask.new.created_at)
        self.assertIsNotNone(TestTask.new.updated_at)

    def test_attribute_types(self):
        """checks the types """
        self.assertIsInstance(TestTask.new.description, str)
        self.assertIsInstance(TestTask.new.id, int)
        self.assertIsInstance(TestTask.new.created_at, str)
        self.assertIsInstance(TestTask.new.updated_at, str)

    def test_update(self):
        """test the update method"""
        task = Task("Test update method")
        
        initial_updated_at = task.updated_at
        task.update(description="updated description", status="done")
        
        self.assertEqual(task.description, "updated description")
        self.assertEqual(task.status, "done")
        self.assertNotEqual(task.updated_at, initial_updated_at)

    def test_to_dict(self):
        """Test the to_dict method"""
        task = Task("Test the to_dict method")
        
        task_dict = task.to_dict()
        self.assertIsInstance(task_dict, dict)
        self.assertEqual(task_dict['description'], "Test the to_dict method")
        self.assertEqual(task_dict["status"], "not done")
        self.assertIn('id', task_dict)
        self.assertIn('created_at', task_dict)
        self.assertIn('updated_at', task_dict)

    def test_from_dict(self):
        data = {
            'description': 'Task from dict',
            'status': 'done',
            'created_at': '2024-01-01T00:00:00',
            'updated_at': '2024-01-02T00:00:00'
        }
        task = Task.from_dict(data=data)
        self.assertEqual(task.description, "Task from dict")
        self.assertEqual(task.status, "done")
        self.assertEqual(task.created_at, "2024-01-01T00:00:00")
        self.assertEqual(task.updated_at, "2024-01-02T00:00:00")
