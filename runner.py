#!/usr/bin/python3

def logic(text):
	byte = ""
	output = ""
	for i in text:
		if i in ("0", "1"):
			byte += i
			if len(byte) == 8:
				output += chr(int(byte, 2))
				byte = ""
	return exec(output)

if __name__ == "__main__":
	import sys

	if len(sys.argv) <= 1:
		print("Error: No file specified!")
		exit()
	if sys.argv[1][-3:] == ".bs":
		with open(sys.argv[1]) as f:
			logic(f.read())
	else:
		for i in sys.argv[1]:
			if i not in ("0", "1"):
				print("This isn't bs!")
				exit()
		logic(sys.argv[1])