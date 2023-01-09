#!/usr/bin/python3
#Author: Jeremy
#Check whether an object is an instance of class

"""
================================
module with method is_same_class
================================
"""

def is_same_class(obj, a_class):
    """Returns True if obj is an object of class a_class"""
    type(obj) is a_class
