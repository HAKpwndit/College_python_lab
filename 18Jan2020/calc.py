#!/usr/bin/python3

add = lambda a,b: a + b
subs = lambda a,b: a - b
div = lambda a,b: a / b
mul = lambda a,b: a * b

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Divide")
print("4.Multiply")

inpt = input("Enter The Choice(1/2/3/4) \n")

if inpt in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if inpt == '1':
    	print(num1, "+", num2, "=", add(num1, num2))

    elif inpt == '2':
        print(num1, "-", num2, "=", subs(num1, num2))

    elif inpt == '3':
        print(num1, "/", num2, "=", div(num1, num2))

    elif inpt == '4':
        print(num1, "*", num2, "=", mul(num1, num2))
       
else:
    print("Invalid Input")


