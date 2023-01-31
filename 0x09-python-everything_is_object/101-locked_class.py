#!/usr/bin/python3
"""
Module Docstring
"""


class LockedClass:
    """
    Only allows instatiation of an attribute named first_name
    The special attribute __slots__ allows to explicitly state which instance attributes are expected for object instances to have.
    """

    __slots__ = ["first_name"]
