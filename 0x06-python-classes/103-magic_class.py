#!/usr/bin/python3
"""
Module Docstring
"""
import math


class MagicClass:
    """
    Class Docstring
    """

    def __init__(self, radius=0):
        """
        Initialize class Docstring
        """
        self.__radius = 0
        if (type(radius) is not int) or (type(radius) is not float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    @property
    def radius(self):
        """
        Property method Docstring
        """
        return self.__radius

    def area(self):
        """
        Public instance method Docstring
        """
        return math.pi * self._radius * self.__radius

    def circumference(self):
        """
        Public instance method Docstring
        """
        return 2 * math.pi * self.__radius
