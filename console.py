#!/usr/bin/python3
"""Defines the AirBnB command interpreter."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB."""
    prompt = '(hbnb) '


if __name__ == '__main__':
    HBNBCommand().cmdloop()
