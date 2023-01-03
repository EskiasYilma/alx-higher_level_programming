#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end="\n" if i >= 100 else ' ')
            continue
        if i % 5 == 0:
            print("Buzz", end="\n" if i >= 100 else ' ')
            continue
        if i % 3 == 0:
            print("Fizz", end="\n" if i >= 100 else ' ')
            continue
        else:
            print(i, end="\n" if i >= 100 else ' ')
            continue

