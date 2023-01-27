#!/usr/bin/python3
"""
This is the matrix_divided module
"""


def matrix_divided(matrix, div):
    """
    This is the matrix_divided function
    """
    new_matrix = []
    if div == 0:
        raise ZeroDivisionError(
            "division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError(
            "div must be a number")
    if (not (isinstance(matrix, list))) or (matrix is None) or \
            (len(matrix) == 0) or (len(matrix[0]) == 0):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    try:

        for i, j in enumerate(matrix):
            if len(matrix[i]) != len(matrix[0]):
                raise TypeError(
                    "Each row of the matrix must have the same size")
            new_matrix.append(j[:])
            for x, y in enumerate(j):
                if not isinstance(y, (int, float)):
                    raise TypeError(
                        "matrix must be a matrix (list of lists) of integers/floats")
                new_matrix[i][x] = round(y / div, 2)
    except Exception:
        raise
    else:
        return new_matrix
