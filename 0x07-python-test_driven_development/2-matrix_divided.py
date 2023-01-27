#!/usr/bin/python3
"""
This is the matrix_divided module
"""


def matrix_divided(matrix, div):
    """
    This is the matrix_divided function
    """
    new_matrix = []
    try:
        if not ((isinstance(matrix, list)) or (isinstance(i, (int, float)) for i in matrix)):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
            return
        if not isinstance(div, (int, float)):
            raise TypeError(
                "div must be a number")
            return
        if div == 0:
            raise ZeroDivisionError(
                "division by zero")
            return
        for i, j in enumerate(matrix):
            if len(matrix[i]) != len(matrix[0]):
                raise TypeError(
                    "Each row of the matrix must have the same size")
                return
        return [[round(h / 3, 2) for h in i] for i in x]
    except Exception:
        raise
