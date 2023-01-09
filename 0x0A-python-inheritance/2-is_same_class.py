#!/usr/bin/python3
"""
Author: Jeremy
================================
module with method is_same_class
================================
"""

def is_same_class(obj, a_class):
    """Returns True if obj is an object of class a_class"""
    return type(obj) is a_class
