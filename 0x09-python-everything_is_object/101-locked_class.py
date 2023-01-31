#!/usr/bin/python3
"""
Module Docstring
"""


class LockedClass:
    """
    Only allows instatiation of an attribute named first_name
    """

    __slots__ = ["first_name"]
