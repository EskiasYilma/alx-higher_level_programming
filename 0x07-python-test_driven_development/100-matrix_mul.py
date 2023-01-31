#!/usr/bin/python3
"""
Module Docstring for matrix_mul(m_a, m_b)

Returns a multiplication of 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    Function to return the multiplication of 2 matrices m_a and m_b
    Checks:
        - if matrices are formatted properly
        - if matrices contain only floats and ints and are not empty
        - if martices are multipliable
        - if martices are of the same size
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
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
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    res = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            mul = 0
            for k in range(len(m_b)):
                mul += m_a[i][k] * m_b[k][j]
            row.append(mul)
        res.append(row)

    return res
