#!/usr/bin/python3
"""
Module Docstring
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Docstring
    """

    def __init__(self, size):
        """
        init docstring
        """
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
