#!/usr/bin/python3
"""
Module Docstring
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Docstring
    """

    def __init__(self, size):
        """
        init docstring
        """
        super().integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, self.__size, self.__size)

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
