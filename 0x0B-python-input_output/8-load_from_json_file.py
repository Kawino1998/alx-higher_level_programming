#!/usr/bin/python3
import json


"""
load_from_json_file function module.

Define load_from_json_file function.
"""


def load_from_json_file(filename):
    """Returns an object from a text file JSON string.
    filename (str): the file to load from.
    """
    with open(filename, 'r', encoding="UTF-8") as myfile:
        return json.loads(myfile.read())
