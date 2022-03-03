import sys
string = sys.argv[1]
n=8
split_string = [string[i:i+n] for i in range(0, len(string), n)]
with open("output.bs", 'a') as f:
	for i in split_string:
		f.write(f"{i}\n")