#!/usr/bin/python3
"""
===================================
module with class BaseGeometry
===================================
"""


class BaseGeometry:
    "Class BaseGeometry"

    def area(self):
        "method for calculated area"

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""

        if type(value) is not int:
            raise TypeError(f'{self.name} must be an integer')
        elif value <= 0:
            raise ValueError(f'{self.name} must be greater than 0')
