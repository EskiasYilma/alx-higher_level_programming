#!/usr/bin/python3
"""
Module Docstring
"""


def append_write(filename="", text=""):
    """
    append_write
    """
    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(text)
