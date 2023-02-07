#!/usr/bin/python3
"""
Module Docstring
"""


def class_to_json(obj):
    """
    class_to_json
    """
    return {key: value for key, value in obj.__dict__.items()
            if type(value) in [list, dict, str, int, bool]}
