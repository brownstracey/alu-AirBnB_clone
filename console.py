#!/usr/bin/python3
"""Command interpreter for HBNB project."""
import cmd
import json
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Command interpreter class for HBNB."""
    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel
    }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program (Ctrl+D)."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel and saves it to the JSON file."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            instance = self.classes[args[0]]()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            objects = models.storage.all()
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            objects = models.storage.all()
            if key in objects:
                del objects[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of instances."""
        args = arg.split()
        objects = models.storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in objects.items() if key.startswith(args[0])])

    def do_update(self, arg):
        """Updates an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            objects = models.storage.all()
            if key not in objects:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                attr_name = args[2]
                attr_value = args[3].strip('"')
                instance = objects[key]
                setattr(instance, attr_name, attr_value)
                instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
