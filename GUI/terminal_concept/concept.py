from msvcrt import getch
import os
import string as sss

def add_zero(binary):
	if len(binary) < 8:
		binary = f"0{binary}"
		binary = add_zero(binary)
	if len(binary) == 8:
		return binary

string = ""
plain = False
final = ""

while True:
	inp = str(getch())[2:-1]
	if inp in sss.ascii_lowercase + sss.ascii_uppercase + r"\x03\r" + " " + sss.punctuation + "1234567890":
		if inp == r"\x03":
			final = final[:-1]
		else:
			final += inp
	if plain == False:
		if inp == r'\x03':
			print("\n\n"+str(exec(final))[:-4], end="")
			exit()
		elif inp == r'\r':
			string += "00001010"
			print(string)
			string = ""
		elif inp == r'\x08':
			string = string[:-9]
			print(f"{(os.get_terminal_size()[0] - 1)*' '}", end="\r")
			print(string[:-1] + " ", end=" \r")
		elif inp == r'\x16':
			plain = True
		else:
			string += str(add_zero(bin(ord(inp))[2:])) + " "
			print(string, end="\r")
	# else:
	# 	if inp == r'\x03':
	# 		exit()
	# 	elif inp == r'\x16':
	# 		plain = False
	# 	else:
	# 		print(inp, end="", flush=True)