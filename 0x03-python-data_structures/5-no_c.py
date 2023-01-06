#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for i in my_string:
        if i in ['c', 'C']:
            continue
        new_str += str(i)
    return new_str
