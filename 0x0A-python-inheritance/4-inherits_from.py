#!/usr/bin/python3
"""
================================
Whether an object is instance of a class
================================
"""

def inherits_from(obj, a_class):
    if isinstance(obj, a_class):
        """Method that return True if an object is an instance of a class
    that inherited from"""
        return True
    return False
