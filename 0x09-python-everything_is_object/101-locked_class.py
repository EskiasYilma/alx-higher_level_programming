#!/usr/bin/python3
"""
Module Docstring
"""


class LockedClass:
    """
    Only allows instatiation of an attribute named first_name
    The special attribute __slots__ allows you to explicitly state which instance attributes you expect your object instances to have, with the expected results
    """

    __slots__ = ["first_name"]
