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
        if type(radius) not in (int, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

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

dis.dis(MagicClass.__init__)
dis.dis(MagicClass.area)
dis.dis(MagicClass.circumference)
