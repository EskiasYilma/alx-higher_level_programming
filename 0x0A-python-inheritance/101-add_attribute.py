#!/usr/bin/python3
"""
Module Docstring
"""


def add_attribute(object, name, attr):
    """
    add_attribute Function
    """
    test_attr = getattr(object, "__doc__", None)
    if test_attr == None:
        setattr(object, name, attr)
    else:
        raise TypeError("can't add new attribute")
