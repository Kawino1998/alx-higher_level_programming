#!/usr/bin/python3
"""
read_file function module.
Define read_file function.
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.
    filename (file):
    """
    with open(filename, encoding='UTF8') as f:
        data = f.read()
        print(data, end='')
