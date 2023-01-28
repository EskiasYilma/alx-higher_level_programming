#!/usr/bin/python3
"""
This is the matrix_divided module

Returns All elements of the matrix divided by div, rounded to 2 decimal places
"""


def matrix_divided(matrix, div):
    """
    matrix_divided Function Docstring
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if (not isinstance(matrix, list)) or (matrix is None) or \
            (len(matrix) == 0) or (len(matrix[0]) == 0):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if any(not isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    new_matrix = [[round(i / div, 2) for i in row] for row in matrix]
    return new_matrix
