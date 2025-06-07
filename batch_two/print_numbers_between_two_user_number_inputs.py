# B2 Prog10: Ask 2 user number inputs. Print the numbers in between.

# Ask user input 
num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))

# For loop to print numbers between two user inputs
for x in range(num1 + 1, num2):
    print(x)