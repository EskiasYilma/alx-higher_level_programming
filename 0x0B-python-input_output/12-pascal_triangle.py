#!/usr/bin/python3
"""
Module Docstring
"""


def pascal_triangle(n):
    """
    pascal_triangle
    """
    if n <= 0:
        return []
    tr = []
    for i in range(n):
        if i == 0:
            tr.append([1])
        else:
            row = [1]
            for j in range(i - 1):
                row.append(tr[i - 1][j] + tr[i - 1][j + 1])
            row.append(1)
            tr.append(row)
    return tr
