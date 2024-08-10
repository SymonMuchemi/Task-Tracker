#!/usr/bin/python3
""" test the Task model """
import unittest
import os
from models.task import Task
from datetime import datetime
from datetime import timedelta


class TestTask(unittest.TestCase):
    __file_path = 'test_data.json'

    @classmethod
    def setUpClass(cls):
        cls.time_now = datetime.now()
        cls.new = Task("Check attributes", "not done")


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
        self.assertIsInstance(TestTask.new.id, str)
        self.assertIsInstance(TestTask.new.created_at, datetime)
        self.assertIsInstance(TestTask.new.updated_at, datetime)
        
    def test_attribute_values(self):
        """ checks the values of attributes """
        created_at_naive = TestTask.new.created_at.replace(tzinfo=None)
        updated_at_naive = TestTask.new.updated_at.replace(tzinfo=None)
        time_difference = abs(created_at_naive - TestTask.time_now)
        time_difference2 = abs(updated_at_naive - TestTask.time_now)
        
        self.assertEqual(TestTask.new.description, "Check attributes")
        self.assertEqual(TestTask.new.status, "not done")
        self.assertEqual(TestTask.new.created_at, TestTask.new.updated_at)
        self.assertLessEqual(time_difference, timedelta(seconds=1))
        self.assertLessEqual(time_difference2, timedelta(seconds=1))
        
        

