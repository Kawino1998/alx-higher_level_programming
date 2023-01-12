#!/usr/bin/python3
# File: 3-to_json_string.py
# Author: Jeremy Kawino
"""Defines a JSON-to-object function."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of
    an object (string).
    """
    return json.dumps(my_obj)
