#!/usr/bin/python3
"""
Module Docstring
"""


class Square:
    """
    Class Docstring
    """

    def __init__(self, size: int = 0):
        """
        Initialize class Docstring
        """
        self.__size = size

    @property
    def size(self):
        """
        Property method Docstring
        """
        return self.__size

    @size.setter
    def size(self, value: int):
        """
        Setter method Docstring
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Public instance method Docstring
        """
        return self.__size * self.__size
