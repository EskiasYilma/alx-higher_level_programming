#!/usr/bin/python3
"""
Module Docstring
"""


def inherits_from(obj, a_class):
    """
    inherits_from Docstring
    Returns True if the object is an instance of a\
    class that inherited (directly or indirectly)\
    from the specified class ; otherwise False
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    return False
