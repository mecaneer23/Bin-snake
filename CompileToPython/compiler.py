#!/bin/python3

with open(f"{sys.argv[1][:-3]}.py", 'w') as g:
	g.write(output)
print(f"Created: {sys.argv[1][:-3]}.py")