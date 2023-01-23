#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        leng = 0
        for i in range(0, x):
            if type(my_list[i]) == int:
                leng += 1
                print("{:d}".format(my_list[i]), end="")
    except TypeError as e:
        print(e)
    else:
        print("")
        return leng
