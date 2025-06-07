# B2 Prog04: Ask 2 user number inputs. 
# Print the quotient without the decimal point.

# Ask for user input
num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))

# Print quotient w/o decimals (whole number only)
if num2 == 0:
    print("Undefined")
else: 
    quotient = num1 / num2
    print(int(quotient))