import os, sys
if os.name == 'nt':
	from msvcrt import getch
else:
	from getch import getch
import re
import pyperclip

def add_zero(binary):
	if len(binary) < 8:
		binary = f"0{binary}"
		binary = add_zero(binary)
	if len(binary) == 8:
		return binary

out = ""
exit_var = False
toggle_space = True
toggle_nl = False

def check_toggles():
	global toggle_space, toggle_nl, out
	if toggle_space == True:
		out += " "
	elif toggle_nl == True:
		out += "\n"

while True:
	char = str(getch())
	if os.name == 'nt':
		if exit_var != True:
			os.system('cls')
		if re.compile(r"^b'[A-Za-z0-9~!@#$%^&*()_+-=`\[\]\\{}\|:\";'<>?,./ ]'$").match(char): # main keys
			char = char[2:-1]
			out += add_zero(str(bin(ord(char)))[2:])
			check_toggles()
		elif char == r"b'\x08'": # backspace
			if toggle_space == True:
				out = out[:-9]
			else:
				out = out[:-8]
		elif char == r"b'\r'": # enter
			out += "00001010"
			check_toggles()
		elif char == r"b'\t'": # tab
			out += "00001001"
			check_toggles()
		elif char in [r"b'\x03'", r"b'\x1b'"]: # ^C | Esc -> exit
			exit_var = True
			exit()
		elif char == r"b'\x13'": # ^S -> save
			pyperclip.copy(out)
			print("\nCopied to clipboard\n")
		elif char == r"b'\x14'": # ^T -> toggle space
			toggle_space = not toggle_space
		elif char == r"b'\x19'": # ^Y -> toggle newline
			toggle_nl = not toggle_nl
		elif char == r"b'\x17'": # ^W -> display help message
			# print(open(sys.argv[0]).read())
			print("^C\texit\n^S\tsave\n^T\ttoggle space\n^Y\ttoggle newline\n^W\tdisplay this message\n")
		print(out)
	else:
		if exit_var != True:
			os.system('clear')
		if re.compile(r"^[A-Za-z0-9~!@#$%^&*()_+-=`\[\]\\{}\|:\";'<>?,./ ]$").match(char): # main keys
			char = char[2:-1]
			out += add_zero(str(bin(ord(char)))[2:])
			check_toggles()
		elif char == r"b'\x08'": # backspace
			if toggle_space == True:
				out = out[:-9]
			else:
				out = out[:-8]
		elif char == r"b'\r'": # enter
			out += "00001010"
			check_toggles()
		elif char == r"b'\t'": # tab
			out += "00001001"
			check_toggles()
		elif char in [r"b'\x03'", r"b'\x1b'"]: # ^C | Esc -> exit
			exit_var = True
			exit()
		elif char == r"b'\x13'": # ^S -> save
			pyperclip.copy(out)
			print("\nCopied to clipboard\n")
		elif char == r"b'\x14'": # ^T -> toggle space
			toggle_space = not toggle_space
		elif char == r"b'\x19'": # ^Y -> toggle newline
			toggle_nl = not toggle_nl
		elif char == r"b'\x17'": # ^W -> display help message
			# print(open(sys.argv[0]).read())
			print("^C\texit\n^S\tsave\n^T\ttoggle space\n^Y\ttoggle newline\n^W\tdisplay this message\n")
		print(out)