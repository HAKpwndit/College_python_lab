#!/usr/bin/python3

c,d=input("\nEnter the value of C and D:").split(" ")
c=int(c)
d=int(d)

c = c+d
d = c-d
c = c-d

print("Enter the value of C and D: {} {}".format(c,d))