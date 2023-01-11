#!/usr/bin/python3
import json
"""
to_json_string function module.
Define to_json_string function.
"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).
    No need to manage exceptions if the object can’t be serialized.
    """
    return json.dumps(my_obj)
