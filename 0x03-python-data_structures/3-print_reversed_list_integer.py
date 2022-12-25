#!/usr/bin/python3
# 3-print_reversed_list_integer.py
# Author: Jeremy


def print_reversed_list_integer(my_list=[]):
    count = len(my_list)-1
    new_list = []
    while count >= 0:
        new_list.append(my_list[count])
        count -= 1
    for i in new_list:
        print("{:d}".format(i))
