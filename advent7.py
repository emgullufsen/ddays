#!/usr/bin/python

# EMG
# Advent of code level seven.
import re

def main():
	fil = open("input7.txt",'r')

	inp = fil.readlines()

	# for lin in inp:
	# 	x = re.search(r'c{1,1}', lin)
	# 	if x:
	# 		print(lin)
	# 		print("\n")

	for i in inp:
		arr = re.findall(r'[a-zA-Z0-9]{1,}',i)
		if (('b' in arr) or ('c' in arr)):
		 	print(arr)

	fil.close()

if __name__ == "__main__":
	main()