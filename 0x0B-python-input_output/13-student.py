#!/usr/bin/python3
""" Student class module
"""


class Student:
    """ Student class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns a dictionary representation of a Student instance.
        attrs (list): (optional) a list of strings to return the attributes of.
        """
        if attrs is None:
            return self.__dict__
        mydict = {}
        for key in attrs:
            if key in self.__dict__.keys():
                mydict[key] = self.__dict__.get(key)
        return mydict

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance
        json (dict): a dictionary where key is attribute and value is value
        """
        for key in json:
            setattr(self, key, json[key])
