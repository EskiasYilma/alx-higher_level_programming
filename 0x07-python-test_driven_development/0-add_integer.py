#!/usr/bin/python3
"""
This is the add_integer module

Returns the sum of two numbers a and b
"""


def add_integer(a, b=98):
    """
    Function Docstring
    """
    try:
        if type(a) not in (int, float):
            raise TypeError("a must be an integer")
            return
        if type(b) not in (int, float):
            raise TypeError("b must be an integer")
        return int(a) + int(b)
    except Exception:
        raise
