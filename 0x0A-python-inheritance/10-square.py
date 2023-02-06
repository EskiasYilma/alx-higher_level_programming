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
        super().__init__(size, size)
