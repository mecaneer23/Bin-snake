#!/bin/python3

import sys

def add_zero(binary):
	if len(binary) < 8:
		return add_zero(f"0{binary}")
	return binary

if len(sys.argv) <= 1:
	print("Error: No file specified!")
	exit()
if sys.argv[1][-3:] != ".py":
	print("This isn't a python file!")
	exit()

with open(sys.argv[1], 'r') as f:
	with open(f"{sys.argv[1][:-3]}.bs", 'w') as g:
		g.write("".join(add_zero(bin(ord(i))[2:]) for i in f.read()))
print(f"Created: {sys.argv[1][:-3]}.bs")
