#!/usr/bin/python3
""" starter file for the application """
import cmd
import sys


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
        args = args.split()

        if len(args) >= 2:
            pass


if __name__ == '__main__':
    TaskCLI().cmdloop()
