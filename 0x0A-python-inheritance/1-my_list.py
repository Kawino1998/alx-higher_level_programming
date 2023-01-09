#!/usr/bin/python3
#Author: Jeremy
#Class MyList inheriting from list

class MyList(list):
    """Class with method - print_sorted"""
    pass

    def print_sorted(self):
        """Method that sorts a list"""

        print(sorted(list(self))
