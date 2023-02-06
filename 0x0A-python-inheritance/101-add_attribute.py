#!/usr/bin/python3
"""
Module Docstring
"""


def add_attribute(object, name, attr):
    """
    add_attribute Function
    """
    if getattr(object, "__doc__", None) is None:
        setattr(object, name, attr)
    else:
        raise TypeError("can't add new attribute")
