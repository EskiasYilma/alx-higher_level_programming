#!/usr/bin/python3
"""
Module Docstring
"""


def read_file(filename=""):
    """
    read_file docstring
    """
    with open(filename, encoding="UTF8") as f:
        print("".join(f.readlines()))
