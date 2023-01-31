#!/usr/bin/python3
"""
Module Docstring
"""


class LockedClass:
    """
    LockedClass Docstring
    """

    def __setattr__(self, key, value):
        """
        Fucntion to check and validate if the passed instance is first_name
        """
        if key != 'first_name':
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(key))
