#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = my_list
    if idx < 0 or idx > len(my_list):
        return new_list
    else:
        del my_list[idx]
        return new_list
