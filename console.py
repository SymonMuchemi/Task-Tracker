#!/usr/bin/python3
""" starter file for the application """
import cmd
import sys
from models.task import Task
from models import storage

states = ['not-done', 'done', 'in-progress']


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

    def do_quit(self):
        """exit the console application"""
        storage.save()
        print("Exiting the console")
        return True

    def do_add(self, args):
        """ Adds a new task """
        desc = args.replace('"', '')

        if len(desc) >= 2:
            new_task = Task(description=desc)
            storage.new(new_task)
            storage.save()
            print(f"Task saved with id: {new_task.id}")
        else:
            print("Usage: add <task description>")

    def do_list(self, args):
        """list tasks
        usage: list
        """
        all_tasks = storage.all()
        print("ID Status Description")
        for task in all_tasks.values():
            print(task)

    def do_mark(self, args):
        """Changes the status of a task"""
        args = args.split()
        print(args)
        task = None
        id = args[0] or None
        new_status = args[1].lower() if args[1] else None
        
        if new_status is None:
            print("Status cannot be empty")

        if len(args) == 2:
            tasks = storage.all()
            print(val for val in tasks.values())
            if id in tasks:
                task = tasks[id]
                print(type(task))
            else:
                print("Task not found")
            
            print(task)
            task.update(status=new_status)
            print(task)
            storage.save()


if __name__ == '__main__':
    TaskCLI().cmdloop()
