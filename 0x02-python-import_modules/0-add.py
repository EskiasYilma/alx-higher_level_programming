#!/usr/bin/python3
from add_0 import add


def my_function():
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))


if __name__ == "__main__":
    import sys
    my_function()
