#!/usr/bin/python3
"""
Module Docstring
"""


class Square:
    """
    Class Docstring
    """

    def __init__(self, size=0):
        """
        Initialize class Docstring
        """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
