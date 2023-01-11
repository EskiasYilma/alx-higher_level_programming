#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    temp = {i: j for i, j in a_dictionary.items()}
    for i, j in temp.items():
        if (value == j):
            a_dictionary.pop(i)
    return a_dictionary
