#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i, j in enumerate(my_list):
        if j == search:
            new_list.append(replace)
        else:
            new_list.append(j)
    return new_list
