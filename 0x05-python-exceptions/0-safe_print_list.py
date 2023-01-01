#!/usr/bin/python3
#Author: Jeremy
#Prints and returs no. of elements in a list

def safe_print_list(my_list, x):
    i = 0

    while i != x:

        try:
            print(my_list[i], end='')
            i += 1

        except:
            continue
    print()
    return i
