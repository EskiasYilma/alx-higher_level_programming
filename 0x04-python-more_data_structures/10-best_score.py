#!/usr/bin/python3
def best_score(a_dictionary):
    best_val = None
    if list(a_dictionary.values())[0]:
        best_val = list(a_dictionary.values())[0]
        for i, j in a_dictionary.items():
            if j > best_val:
                best_val = j

    return best_val
