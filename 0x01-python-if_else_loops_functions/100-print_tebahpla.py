#!/usr/bin/python3
for i in reversed(range(ord('a'), ord('z') + 1)):
    print("{:c}".format(i) if i % 2 == 0 else "{:c}".format(i - 32), end='')
