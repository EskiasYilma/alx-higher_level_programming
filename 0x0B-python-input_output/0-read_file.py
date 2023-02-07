#!/usr/bin/python3
"""
Module Docstring
"""


def read_file(filename=""):
    with open(filename, encoding="UTF8") as f:
        print("".join(f.readlines()))
