#!/usr/bin/python3
# 6-print_sorted_dictionary.py
# Author: Jeremy


def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys."""
    for key, value in sorted(a_dictionary.items()):
    print(f"{key}: {value}")
