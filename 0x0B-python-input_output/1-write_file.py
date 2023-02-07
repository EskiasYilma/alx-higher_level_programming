#!/usr/bin/python3
"""
Module Docstring
"""


def write_file(filename="", text=""):
    """
    write_file
    """
    with open(filename, 'w', encoding="UTF8") as f:
        return f.write(text)
