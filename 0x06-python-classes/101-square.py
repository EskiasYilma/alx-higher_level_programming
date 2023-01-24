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
        self.size = size
        self.position = position

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
        if (type(value) != tuple) or (len(value) != 2) or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        """
        Public instance method Docstring
        """
        square = ""
        if self.__size == 0:
            return square
        for i in range(self.__position[1]):
            square += "\n"
        for i in range(self.__size):
            square += (" " * self.__position[0])
            square += ("#" * self.__size)
            if i is not (self.__size - 1):
                square += "\n"
        return square

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
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __repr__(self):
        """
        Public instance method Docstring
        """
        return self.__str__()
