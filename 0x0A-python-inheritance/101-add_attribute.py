#!/usr/bin/python3
"""
Module Docstring
"""


def add_attribute(test_object, test_name, test_attr):
    """
    add_attribute Function
    """
    test_attr = getattr(test_object, "__doc__", None)
    if test_attr == None:
        setattr(test_object, test_name, test_attr)
    else:
        raise TypeError("can't add new attribute")
