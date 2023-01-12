#!/usr/bin/python3
# File: 3-to_json_string.py
# Author: Jeremy Kawino

import json
"""
to_json_string function module.
Define to_json_string function.
"""


def to_json_string(my_obj):
    """Returns the JSON representation of
    an object (string).
    """
    return json.dumps(my_obj)
