#!/usr/bin/python3
"""Tests the storage engine"""
import unittest
import json
import os
from models.engine.storage import File_storage
from models.task import Task

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = File_storage()
        self.storage._File_storage__file_path = 'test_tasks.json'
        self.storage._File_storage__objects = {}

    def tearDown(self):
        if self.storage is not None:
            del self.storage
            
        if os.path.exists('test_tasks.json'):
            os.remove('test_tasks.json')

    def test_all_empty(self):
        self.assertEqual(self.storage.all(), {})

    def test_all_with_objects(self):
        task = Task("Test task")
        self.storage.new(task)
        self.assertEqual(len(self.storage.all()), 1)
        self.assertIn(task.id, self.storage.all())

    def test_all_with_id(self):
        task1 = Task("Task 1")
        task2 = Task("Task 2")
        self.storage.new(task1)
        self.storage.new(task2)
        self.assertEqual(len(self.storage.all(task2.id)), 1)
        self.assertIn(task1.id, self.storage.all(task1.id))

    def test_new(self):
        task = Task("New task")
        self.storage.new(task)
        self.assertIn(task.id, self.storage._File_storage__objects)

    def test_save_and_load(self):
        task = Task("Save and load task")
        self.storage.new(task)
        self.storage.save()
        
        new_storage = File_storage()
        new_storage._File_storage__file_path = 'test_tasks.json'
        new_storage.load()
        
        self.assertIn(task.id, new_storage.all())
        for task in new_storage.all():
            print(task)
            
        loaded_task = new_storage.all()[task.id]
        self.assertEqual(loaded_task.description, "Save and load task")

    def test_load_file_not_found(self):
        self.storage.load()

    def test_save_empty(self):
        self.storage.save()
        with open('test_tasks.json', 'r') as f:
            data = json.load(f)
        self.assertEqual(data, {})

    def test_close(self):
        # This test is a bit tricky as 'close' just calls 'reload'
        # which is not defined in the provided code.
        # You might want to modify this based on your actual implementation
        with self.assertRaises(AttributeError):
            self.storage.close()

if __name__ == '__main__':
    unittest.main()
