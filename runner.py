#!/bin/python3

import sys

def logic(text):
	temp = ""
	counter = 0
	chars = []
	output = ""
	for i in text:
		if i in ["0", "1"]:
			temp += i
			counter += 1
			if counter == 8:
				chars.append(temp)
				temp = ""
				counter = 0
	for i in chars:
		output += chr(int(i, 2))
	print(str(exec(output))[:-4], end="")
try:
	if sys.argv[1][-3:] == ".bs":
		with open(sys.argv[1]) as f:
			logic(f.read())
	else:
		for i in sys.argv[1]:
			if i not in ["0", "1"]:
				print("This isn't bs!")
				exit()
		logic(sys.argv[1])
except IndexError:
	print("Make sure to include a Bin-snake file, for example: ", end="")
	if sys.argv[0] == "runner.py":
		if sys.platform == "win32":
			print(f"python runner.py filename.bs")
		else:
			print(f"python3 runner.py filename.bs")
	elif sys.argv[0] == "runner.exe":
		print(f"runner.exe filename.bs")
	else:
		print("Failed to run")
