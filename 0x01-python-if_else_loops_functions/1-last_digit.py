#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_d = int(str(number)[-1])
if last_d < 6 and last_d != 0:
    print(
        f"Last digit of {number:d} is {last_d:d} and is less than 6 and is not 0")
elif last_d == 0:
    print(f"Last digit of {number:d} is {last_d:d} and is 0")
elif last_d > 5:
    print(f"Last digit of {number:d} is {last_d:d} and is greater than 5")
