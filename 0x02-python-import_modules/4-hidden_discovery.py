#!/usr/bin/python3
import hidden_4


def my_func():
    for i in dir(hidden_4):
        if "__" in i:
            continue
        print(i)


if __name__ == "__main__":
    import sys
    my_func()
