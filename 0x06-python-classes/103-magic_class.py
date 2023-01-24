#!/usr/bin/python3
"""
Module Docstring
"""
import dis
import math


class MagicClass:
    """
    Class Docstring
    """

    def __init__(self, radius):
        """
        Initialize class Docstring
        """
        self.__radius = radius

    @property
    def radius(self):
        """
        Property method Docstring
        """
        return self.__radius

    @radius.setter
    def radius(self, value):
        """
        Setter method Docstring
        """
        if type(value) not in (int, float):
            raise TypeError("radius must be a number")
        self.__radius = value

    def area(self):
        """
        Public instance method Docstring
        """
        return math.pi * (self._radius ** 2)

    def circumference(self):
        """
        Public instance method Docstring
        """
        return 2 * math.pi * self.__radius
