#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def my_func(argv):
    op_dict = {'+': add, '-': sub, '*': mul, '/': div}
    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    if op not in op_dict:
        print("Unknown operator. Only: +, -, * and / available")
        exit(1)
    print('{:d} {} {:d} = {:d}'.format(a, op, b, op_dict[op](a, b)))


if __name__ == "__main__":
    import sys
    my_func(sys.argv)
