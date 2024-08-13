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
        storage.save()
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

    def do_list(self, args):
        """list tasks """
        n = len(args)
        print(args if n == 0 else '')
        if n == 0:
            all_tasks = storage.all()
            print(len(all_tasks))
            print(type(all_tasks))
            print("ID  Status\t Description")
            for key, task in all_tasks.items():
                print(task)


if __name__ == '__main__':
    TaskCLI().cmdloop()
