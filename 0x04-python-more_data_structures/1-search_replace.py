#!/usr/bin/python3
# 1-search_replace.py
# Author: Jeremy

def search_replace(my_list, search, replace):
    #Replaces all occurences of search
    b = [x if x != search else replace for x in my_list]
    return b
