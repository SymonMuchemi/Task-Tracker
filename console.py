#!/usr/bin/python3
""" starter file for the application """
import cmd
from models.task import Task
from models import storage

states = ['not-done', 'done', 'in progress']


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
        args = args.split()
        all_tasks = storage.all()
        filtered_tasks = []
        
        if len(args) == 0:
            print("ID Status Description")
            for task in all_tasks.values():
                print(task)

        else:
            query_status = args[0].lower()
            if query_status in states:
                for task in all_tasks.values():
                    if task.status == query_status:
                        filtered_tasks.append(task)
                for task in filtered_tasks:
                    print(task)

    def do_mark(self, args):
        """Changes the status of a task
        Usage: mark <id> <done|in-progress|not-done>
        """
        args = args.split()

        if len(args) < 2:
            print("Usage: mark <id> <new status>")

        task_id = int(args[0])
        new_status = args[1].lower()
        new_status = new_status.replace('-', ' ')

        if new_status not in states:
            print("Invalid status!", end='')
            print(" status must be:not done, done or in progress")

        tasks = storage.all(id=task_id)
        if tasks:
            task = tasks[task_id]
            task.update(status=new_status)
            storage.save()
            print(f"Task {task_id} updated to {new_status}")
        else:
            print(f"No task found with id {task_id}")


if __name__ == '__main__':
    TaskCLI().cmdloop()
