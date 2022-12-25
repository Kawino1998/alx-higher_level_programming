#!/usr/bin/python3
# 9-max_integer.py
# Author: Jeremy


def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if len(my_list) == 0:
        return (None)

    max_number = my_list[0]
    for a in my_list:
        if a > max_number:
            max_number = a
    return max_number
