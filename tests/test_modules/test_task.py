#!/usr/bin/python3
""" test the Task model """
import unittest
from models.task import Task


class TestTask(unittest.TestCase):
    def setUp(self) -> None:
        task = Task()
