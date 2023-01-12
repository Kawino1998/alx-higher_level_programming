#!/usr/bin/python3
#File: 5-save_to_json_file.py
#Author: Jeremy Kawino
""" Defines a JSON file writing function"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, mode="w") as myfile:
        myfile.write(json.dumps(my_obj))
