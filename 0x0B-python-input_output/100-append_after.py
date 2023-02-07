#!/usr/bin/python3
"""
Module Docstring
"""


def append_after(filename="", search_string="", new_string=""):
    """
    append_after
    """
    data = ""
    with open(filename, "r") as f:
        for line in f:
            data += line
            if search_string in line:
                data += new_string
    with open(filename, "w") as f:
        f.write(data)
