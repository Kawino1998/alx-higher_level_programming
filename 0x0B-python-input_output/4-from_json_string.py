#!/usr/bin/python3
#Author: Jeremy Kawino
#File: 4-from_json_string.py
"""Define object to JSON string"""
import json


def from_json_string(my_str):
    """Returns an object made from JSON string.
    my_str: the string to load from JSON.
    """
    return json.loads(my_str)
