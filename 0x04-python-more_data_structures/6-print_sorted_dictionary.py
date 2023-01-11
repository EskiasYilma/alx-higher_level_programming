#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i in sorted([keys for keys, val in a_dictionary.items()]):
        print("{}: {}".format(i, a_dictionary[i]))
