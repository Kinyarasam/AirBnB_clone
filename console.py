#!/usr/bin/python3
""" contains the entry point of the command interpreter """
import cmd

class HBNBCommand(cmd.Cmd):
    """ class that implements the console
    for the airBnB clone web application
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """execute when an empty line + <ENTER> key """
        pass

    def do_EOF(self, argv):
        """ EOF signal to exit the program """
        print("")
        return True

    def do_quit(self, argv):
        """Quit command to exit the program 
        """
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
