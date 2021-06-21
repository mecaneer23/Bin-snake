#!/bin/python3

# takes a file that is completely ones and zeros - any non-valid character is treated as a comment
# outputs python output

import sys, os

if sys.argv[1][-3:] == ".bs":
	with open(sys.argv[1]) as f:
		temp = ""
		counter = 0
		chars = []
		output = ""
		for i in f.read():
			if i in ["0", "1"]:
				temp += i
				counter += 1
				if counter == 8:
					chars.append(temp)
					temp = ""
					counter = 0
		for i in chars:
			output += chr(int(i, 2))
		with open("temp.py", 'w') as g:
			g.write(output)
		print(os.popen("python temp.py" if os.name == 'nt' else "python3 temp.py").read(), end="")
		os.system("del temp.py" if os.name == 'nt' else "rm temp.py")
else:
	print("This isn't bs!")
	exit()
