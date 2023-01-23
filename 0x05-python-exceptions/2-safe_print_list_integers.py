#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    leng = 0
    try:
        for i in range(0, x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                leng += 1
    except Exception as e:
        print(e)
    else:
        print("")
        return leng
