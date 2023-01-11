#!/usr/bin/python3
"""
write_file function module.
Define write_file function.
"""


def append_file(filename="", text=""):
    """Appends a string to a text file (UTF8).
    filename (str): the file, must have permissions, will create if nonexist.
    text (str): text, will overwrite content of file if already exists.
    Returns: the number of characters added.
    """
    with open(filename, 'a', encoding="UTF-8") as myfile:
        return myfile.write(text)
