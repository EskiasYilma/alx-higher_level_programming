#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if len(str(abs(number))) == 1:
    x = number
elif number == 0:
    x = 0
else:
    x = int(str(number)[-1])

if number < 0:
    x = x * -1

if x < 6:
    if x != 0:
        print(
            f"Last digit of {number} is {x} and is less than 6 and not 0")
    if x == 0 and number == 0:
        print(f"Last digit of {number} is {x} and is 0")
    if x == 0 and number != 0:
        print(
            f"Last digit of {number} is {x} and is less than 6 and is 0")

elif x > 5:
    print(f"Last digit of {number} is {x} and is greater than 5")
