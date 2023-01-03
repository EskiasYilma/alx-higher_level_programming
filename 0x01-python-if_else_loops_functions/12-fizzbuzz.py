#!/usr/bin/python3
def fizzbuzz():
	for i in range(1, 101):
		if i % 5 == 0 and i % 3 == 0:
			print("FizzBuzz", end="\n" if i == 100 else ' ')
			# continue
		elif i % 5 == 0:
			print("Buzz", end="\n" if i == 100 else ' ')
			# continue
		elif i % 3 == 0:
			# print("true")
			print("Fizz", end="\n" if i == 100 else ' ')
			# continue			
		else:
			print(i, end="\n" if i == 100 else ' ')
	