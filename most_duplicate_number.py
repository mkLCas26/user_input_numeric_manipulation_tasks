# B4 Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.
 
"""
Initialize empty lists or needed variables
while loop for user input
    Try-except for determining invalid inputs
    Determining most duplicates from user input
    Print number with most duplicate
"""

numbers = []
num = 0

while True:
    user_input = input("\nEnter a number: ")
    try: 
        num = float(user_input)
    except ValueError:
        print(f"Invalid! {user_input} may not be a number or it is a number list.")
        break