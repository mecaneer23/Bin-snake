#!/bin/python3

# takes a python file - outputs bin-snake file (.bs)

import sys

def add_zero(binary):
	if len(binary) < 8:
		binary = f"0{binary}"
		binary = add_zero(binary)
	if len(binary) == 8:
		return binary

if sys.argv[1][-3:] == ".py":
	pass
else:
	print("This isn't a python file!")
	exit()

with open(sys.argv[1]) as f:
	output = ""
	for i in f.read():
		binary = bin(ord(i))[2:]
		output += add_zero(binary)+"\n"
with open(f"{sys.argv[1][:-3]}.bs", 'w') as g:
	g.write(output)
print(f"Created: {sys.argv[1][:-3]}.bs")