#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    temp = []
    for i in matrix:
        temp.append([j*j for j in i])
    return temp
