#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best_val = int(list(a_dictionary.values())[0])
        best_key = list(a_dictionary.keys())[0]
        for i, j in a_dictionary.items():
            if j > best_val:
                best_val = j
                best_key = i
    else:
        best_key = None
    return best_key
