import os
import re

def move_cursor(y, x):
	os.system("tput cup " + str(y) + " " + str(x))

def print_49(n, s):
	move_cursor(n, 49)
	print(s)

	return n+1


def breakline_49(n, width, text):
	lines = []
	for i in range(0, len(text), width):
		lines.append(text[i:i+width])

	for l in lines:
		print_49(n, l)
		n+=1

	return n

    #return '\n'.join(lines)
	#return re.sub("(.{" + str(width) + "})", "\\1\n", text, 0, re.DOTALL)
