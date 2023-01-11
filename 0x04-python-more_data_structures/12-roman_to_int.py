#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_to_int_dict = {'I': 1, 'V': 5, 'X': 10,
                       'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    x = 0
    i = 0
    if roman_string is None or type(roman_string) != str:
        x = 0
    else:
        while (i < len(roman_string)):
            temp1 = rom_to_int_dict[roman_string[i]]
            if (i + 1 < len(roman_string)):
                temp2 = rom_to_int_dict[roman_string[i + 1]]
                if (temp1 >= temp2):
                    x += temp1
                    i += 1
                else:
                    x += temp2 - temp1
                    i += 2
            else:
                x += temp1
                i += 1
    return x
