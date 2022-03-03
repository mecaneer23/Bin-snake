def add_zero(binary):
	if len(binary) < 8:
		binary = f"0{binary}"
		binary = add_zero(binary)
	if len(binary) == 8:
		return binary

with open("test.bs", 'w') as f:
	for i in range(256):
		binary = bin(i)[2:]
		f.write(str(i)+" = "+add_zero(binary)+"\n")