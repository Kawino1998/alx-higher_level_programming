#!/usr/bin/python3
"""
===================================
module with class Rectangle
===================================
"""


class Rectangle(BaseGeometry):
    """Class Rectangle inheriting from BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
