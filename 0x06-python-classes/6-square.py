#!/usr/bin/python3
"""
Module Docstring
"""


class Square:
    """
    Class Docstring
    """

    def __init__(self, size: int = 0, position: tuple = (0, 0)):
        """
        Initialize class Docstring
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Property method Docstring
        """
        return self.__position

    @position.setter
    def position(self, value: tuple):
        """
        Setter method Docstring
        """
        if type(value) != tuple or len(value) != 2 or \
                not all([type(i) == int for i in value]) or \
                not all([i >= 0 for i in value]):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Public instance method Docstring
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Public instance method Docstring
        """
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
