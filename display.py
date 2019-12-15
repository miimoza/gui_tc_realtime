import os

def move_cursor(y, x):
	os.system("tput cup " + str(y) + " " + str(x))

def print_49(n, s):
	move_cursor(n, 49)
	print(s)

	return n+1
