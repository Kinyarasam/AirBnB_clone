#!/usr/bin/python3
""" contains the entry point of the command interpreter """
import cmd
import re
from shlex import split
import models
from models.base_model import BaseModel


# A global constant since both functions within and outside uses it.
CLASSES = [
        "BaseModel"
]


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


def check_args(args):
    """check if args is valid

    Args (str):
        The string containing the arguements passed to a command

    Returns:
        Error message if args is None or not a valid class, else the arguments
    """
    arg_list = parse(args)

    if len(arg_list) == 0:
        print("** class name missing **")
    elif arg_list[0] not in CLASSES:
        print("** class doesn't exist **")
    else:
        return arg_list


class HBNBCommand(cmd.Cmd):
    """ class that implements the console
    for the airBnB clone web application
    """
    prompt = "(hbnb) "
    storage = models.storage

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

    def default(self, arg):
        """default behaviour for the cmd module when input is invalid"""
        action_map = {
                "all": self.do_all,
                "show": self.do_show,
                "create": self.do_create
        }

        match = re.search(r"\.", arg)
        if match:
            arg1 = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg1[1])
            if match:
                command = [arg1[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in action_map:
                    call = "{} {}".format(arg1[0], command[1])
                    return action_map[command[0]](call)

        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_all(self, argv):
        """Prints all string representation of all instances """
        arg_list = split(argv)
        objects = self.storage.all().values()
        if not arg_list:
            print([str(obj) for obj in objects])
        else:
            if arg_list[0] not in CLASSES:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects if arg_list[0] in str(obj)])

    def do_create(self, argv):
        """Creates a new instance of BaseModel
        saves it (to a JSON file) and
        prints the id
        """
        args = check_args(argv)
        if args:
            print(eval(args[0])().id)
            self.storage.save()

    def do_show(self, argv):
        """Prints the string representation of an nstance based
        on the class name and id
        """
        args = check_args(argv)
        if args:
            if len(args) != 2:
                print("** instance id missing **")
            else:
                key = "{} {}".format(args[0], args[1])
                if key not in self.storage.all():
                    print("** no instance found **")
                else:
                    print(self.storage.all()[key])

if __name__ == "__main__":
    HBNBCommand().cmdloop()