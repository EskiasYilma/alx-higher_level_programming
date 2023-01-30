#!/usr/bin/python3
"""
Module Docstring for matrix_mul(m_a, m_b)

Returns a multiplication of 2 matrices
"""
import numpy as np


def matrix_mul(m_a, m_b):
    """
    Function to return the multiplication of 2 matrices m_a and m_b
    Checks:
        - if matrices are formatted properly
        - if matrices contain only floats and ints and are not empty
        - if martices are multipliable
        - if martices are of the same size
    """

    if isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_a or any(not row for row in m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or any(not row for row in m_b):
        raise ValueError("m_b can't be empty")
    if not all(all(isinstance(i, (int, float)) for i in row) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not all(all(isinstance(i, (int, float)) for i in row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")
    if len(set(len(row) for row in m_a)) != 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(len(row) for row in m_b)) != 1:
        raise TypeError("each row of m_b must be of the same size")
    res = []
    try:
        res = np.dot(m_a, m_b)
    except Exception:
        raise ValueError("m_a and m_b can't be multiplied")
    return res

# m_a = None
# m_b = [[1, 2], [3, 4]]
# Traceback (most recent call last):
# ValueError: m_a can't be empty

# m_b = None
# m_a = [[1, 2], [3, 4]]
# Traceback (most recent call last):
# ValueError: m_b can't be empty


# m_a = [[1, 2], [3, 4]]
# m_b = [[1, 2], [3, 4]]
# print(matrix_mul(m_a, m_b))
# [[ 7 10]
#  [15 22]]

# m_a = [[1, 2]]
# m_b = [[3, 4], [5, 6]]
# print(matrix_mul(m_a, m_b))
# [[13, 16]]

# m_a = [[1, 2, 3]]
# m_b = [[1, 2], [3, 4]]
# Traceback (most recent call last):
# ValueError: m_a and m_b can't be multiplied

# m_a = [[1, 2], [3, 4]]
# m_b = [[1, 2, 3], [4, 5]]
# Traceback (most recent call last):
# TypeError: each row of m_b must be of the same size

# m_a = [[1, 2], [4, 5], [6, 7]]
# m_b = [[1, 2, 3], [4, 5, 6]]
# print(matrix_mul(m_a, m_b))
# [[ 9 12 15]
#  [24 33 42]
#  [34 47 60]]


# m_b = [[1, 2], [3, 4]]
# m_a = m_b
# [[ 7 10]
#  [15 22]]

# m_b = [[1, 2], [3, 4, 5]]
# print(matrix_mul(m_a, m_b))
# Traceback (most recent call last):
# NameError: name 'm_a' is not defined. Did you mean: 'm_b'?

# m_a = []
# m_b = [[1, 2], [3, 4]]
# print(matrix_mul(m_a, m_b))
# Traceback (most recent call last):
# ValueError: m_a can't be empty

# m_a = [[1, 2], [3, 4]]
# m_b = [[1, 2], [3, 4]]
# print(matrix_mul(m_a, m_b))
# [[ 7 10]
#  [15 22]]

# m_a = [[1, 2]]
# m_b = [[3, 4], [5, 6]]
# print(matrix_mul(m_a, m_b))
# [[13, 16]]

# m_a = []
# m_b = [[1, 2], [3, 4]]
# Traceback (most recent call last):
# ValueError: m_a can't be empty

# m_a = [[]]
# m_b = [[1, 2], [3, 4]]
# Traceback (most recent call last):
# ValueError: m_a can't be empty

# m_b = []
# m_a = [[1, 2], [3, 4]]
# Traceback (most recent call last):
# ValueError: m_b can't be empty

# m_b = [[]]
# m_a = [[1, 2], [3, 4]]
# Traceback (most recent call last):
# ValueError: m_b can't be empty


# m_a = [[1, -2], [3, 4]]
# m_b = [[1, 2], [3, -4]]
# [[ -5  10]
#  [ 15 -10]]

# m_a = [[2]]
# m_b = [[2]]
# [[4]]


# m_a = [[2, 3, 4]]
# m_b = [[5, 6, 7]]
# Traceback (most recent call last):
# ValueError: m_a and m_b can't be multiplied

# m_a = [[1], [2]]
# m_b = [[4], [5]]
# Traceback (most recent call last):
# ValueError: m_a and m_b can't be multiplied

# m_a = [[1], [2], [3]]
# m_b = [[2, 3, 4]]
# [[ 2  3  4]
#  [ 4  6  8]
#  [ 6  9 12]]

# m_a = [[1], [2], [3]]
# m_b = [[4], [5], [6]]
# Traceback (most recent call last):
# ValueError: m_a and m_b can't be multiplied
print(matrix_mul(m_a, m_b))
