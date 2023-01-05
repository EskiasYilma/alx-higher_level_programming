#!/usr/bin/python3
def my_func(argv):
    if argv:
        if (len(argv) == 1):
            print("{} arguements".format(len(argv) - 1))
        elif (len(argv) == 2):
            print("{} arguement:".format(len(argv) - 1))
            print("{}: {}".format(len(argv) - 1, argv[1]))
        else:
            print("{} arguements:".format(len(argv) - 1))
            for i in range(1, len(argv)):
                print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    import sys
    my_func(sys.argv)
