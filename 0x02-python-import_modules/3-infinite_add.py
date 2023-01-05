#!/usr/bin/python3
def my_func(argv):
    if argv:
        if (len(argv) == 1):
            print("{}".format(len(argv) - 1))
        elif (len(argv) > 1):
            sum = 0
            for i in range(1, len(argv)):
                sum += int(argv[i])
            print(sum)


if __name__ == "__main__":
    import sys
    my_func(sys.argv)
