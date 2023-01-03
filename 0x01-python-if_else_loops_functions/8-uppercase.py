#!/usr/bin/python3
def uppercase(str):
	for i, j in enumerate(str):
		if ord(j) >= 97 and ord(j) <= 122:
			print('{:c}'.format(ord(j)-32), end="\n" if i == len(str)-1 else '')
		else:
			print('{:c}'.format(ord(j)), end="\n" if i == len(str)-1 else '')