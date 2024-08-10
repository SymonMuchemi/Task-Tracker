import cmd
import sys


class TaskCLI(cmd.Cmd):
    prompt = 'task-cli '
    file = 'tasks.json'
    
    def do_greet(self, args):
        """Prints a greeting message"""
        # if args == "greet":
        print("Hello there, I am your task tracker\n")
        
    def do_EOF(self):
        """Exits the console application"""
        return True

if __name__ == '__main__':
    TaskCLI().cmdloop()
