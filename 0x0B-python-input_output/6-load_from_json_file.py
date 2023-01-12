#!/usr/bin/python3
#File: 6-load_from_json_file.py
#Author: Jeremy Kawino
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename, mode="r") as myfile:
        return json.loads(myfile.read())
