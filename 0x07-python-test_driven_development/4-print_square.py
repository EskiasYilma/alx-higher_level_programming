#!/usr/bin/python3
"""
This is the print_square module

Returns prints a square of size "size" with the character #
"""


def print_square(size):
    """
    Function to print a square of size "size" using the character "#"
    Checks:
        - If size is of type integer
        - If size is greater than Zero and of type float
        - If size equals Zero
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if (isinstance(size, float)) and (size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    else:
        for i in range(size):
            print("#" * size)
