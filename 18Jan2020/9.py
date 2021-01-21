#!/usr/bin/python3

while True:
	st = input("\nEnter the Two Digit Number: ")
	if len(st)==2:
		rev_st = st[::-1]
		print("Reverse of the given number is: {}".format(rev_st))
		exit()
	else:
		print("Please Enter a two Digit Number \n")