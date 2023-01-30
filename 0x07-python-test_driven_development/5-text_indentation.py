#!/usr/bin/python3
"""
This is the print_square module

Returns prints a square of size "size" with the character #
"""


def text_indentation(text):
    """
    print_square Function docstring
    """
    if not isinstance(text, str) or len(text) < 0:
        raise TypeError("text must be a string")
    new_txt = ""
    for i in text:
        if i in [".", "?", ":"]:
            new_txt += i + "\n\n"
        else:
            new_txt += i
    print("\n".join([line.strip() for line in new_txt.split("\n")]), end="")
