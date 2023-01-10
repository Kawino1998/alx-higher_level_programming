#!/usr/bin/python3
import json


"""
to_json_string function module.

Define to_json_string function.
"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).
    my_obj: the object to dump into JSON.
    """
    return json.dumps(my_obj)
