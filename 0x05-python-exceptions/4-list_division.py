#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div = 0
    div_list = []
    # try:
    for i in range(list_length):
        try:
            if list_length > len(my_list_2) and list_length > len(my_list_1):
                print("out of range")
                div = 0
                div_list.append(div)
                continue
            if type(my_list_1[i]) not in [int, float]:
                print("wrong type")
                div = 0
                div_list.append(div)
                continue
            if type(my_list_2[i]) not in [int, float]:
                print("wrong type")
                div = 0
                div_list.append(div)
                continue
            if my_list_2[i] == 0:
                print("division by 0")
                div = 0
                div_list.append(div)
                continue
            else:
                div = my_list_1[i] / my_list_2[i]
                div_list.append(div)

        except IndexError:
            print("out of range")
            div = 0
            div_list.append(div)
        finally:
            pass

    return div_list
