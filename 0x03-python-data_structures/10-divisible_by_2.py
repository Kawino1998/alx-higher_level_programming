#!/usr/bin/python3
# 10-divisible_by_2.py
# Author: Jeremy

def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    multiples = []
    for a in my_list:
        if a % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return multiples
