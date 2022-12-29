#!/usr/bin/python3
# 1-search_replace.py
# Author: Jeremy

def search_replace(my_list, search, replace):
    """Replaces all occurrences of search"""
    return list([x if x != search else replace for x in my_list])
