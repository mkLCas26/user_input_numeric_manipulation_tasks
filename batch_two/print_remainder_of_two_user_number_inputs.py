# B2 Prog05: Ask 2 user number input. Print the remainder.

# Ask user input
num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))

# Divide and print remainder
if num2 == 0:
    print("Undefined")
else:
    remainder = num1 % num2
    print(remainder)