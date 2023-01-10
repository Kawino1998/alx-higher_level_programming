#!/usr/bin/python3
"""
append_write function module.

Define append_write function.
"""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8).
    filename (str): the file, must have permissions, will create if nonexist.
    text (str): text, will be appended at the end.

    Returns: the number of characters written.
    """
    with open(filename, 'a', encoding="UTF-8") as myfile:
        return myfile.write(text)
