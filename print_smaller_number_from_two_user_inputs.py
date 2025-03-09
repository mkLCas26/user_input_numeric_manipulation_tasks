# B2 Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

# Ask user input
num1 = float(input("First Number: "))
num2 = float(input("Second  Number: "))

# If-else statement for determining the smaller number
if num1 < num2: 
    print(num1)
else:
    print(num2)