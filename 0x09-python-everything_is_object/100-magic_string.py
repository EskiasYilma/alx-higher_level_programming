#!/usr/bin/python3
def magic_string():
    magic_string.cnt = getattr(magic_string, 'cnt', 0) + 1
    return ", ".join(["BestSchool" for x in range(magic_string.cnt)])


for i in range(10):
    print(magic_string())
