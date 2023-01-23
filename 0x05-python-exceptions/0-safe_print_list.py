#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    leng = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            leng += 1
        except Exception as e:
            break
    print("")
    return leng
