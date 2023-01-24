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

    def __init__(self, radius=0):
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
        if not isinstance(value, (int, float)):
            raise TypeError("radius must be a number")
        if value < 0:
            raise ValueError("radius must be greater than or equal to 0")
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
