#!/usr/bin/python3
"""Module 12"""


class Student:
    """Class Student"""
    def __init__(self, first_name, last_name, age):
        """Init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method to_json"""
        requested = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            if i in self.__dict__.keys():
                requested[i] = self.__dict__[i]
        return requested
