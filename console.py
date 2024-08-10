#!/usr/bin/python3
""" starter file for the application """
import cmd
import sys
from models.task import Task
from models import storage


class TaskCLI(cmd.Cmd):
    prompt = 'task-cli '
    file = 'tasks.json'

    def do_greet(self, args):
        """Prints a greeting message"""
        print("Hello there, I am your task tracker\n")

    def do_EOF(self):
        """Exits the console application"""
        return True

    def do_add(self, args):
        """ Adds a new task """
        desc = args.replace('"', '')

        if len(args) >= 2:
            new_task = Task(description=desc)
            storage.reload()
            storage.new(new_task)
            storage.save()

            print(f"Task saved with id: {new_task.id}")


if __name__ == '__main__':
    TaskCLI().cmdloop()
