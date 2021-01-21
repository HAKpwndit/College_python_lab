#!/usr/bin/python3


import os

string = """ \n\n\n\n
Assingment 1 by Soummya Mukhopadhyay

The Programs are as follows:
________________________________________________________________
|Sl. No.   | Name of the Program                                 
-----------------------------------------------------------------
|	1 | Write a program to print your name.

|	2 | Write a program to take input marks of 
			two subject and print aggregate.

|	3 | Write a program to calculate area
			of a circle with radius 2.

|	4 | Write a program to calculate area of a circle
			and input for radius through keyboard.

|	5 | Write a program to add two numbers(Input
			through keyboard) and display its sum.

|	6 | Write a program to calculate simple
			interest for a given principal, rate of
			interest, and time.

|	7 | Write a C program to convert temperature
			Farenhite to Celcius.

|	8 | Two numbers are input through the
			keyboard into two location C and D. Write
			a program to interchange the contents of C and D.

|	9 | If two digit number is input through the
			keyboard. Write a program to reverse the
			number.
---------------------------------------------------------------------
""" 



def main():
	
	while True:
		print(string +"\n")
		opt = int(input("Enter The 'Sl. No.' from the above list to run the program: \n"))
	
		os.system("./{}.py".format(opt))
		print("\n\n\nEnter crtl+c To exit 1")
		boo = input("\nor To Continue Press any key  ")

		
if __name__ == '__main__':
	main()



