# B4 Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

"""
Initialize empty list or needed variables
While loop for user input
    Try-except to determine invalid inputs
    Determine highest number using if-else
    Print the highest number
"""

highest = None
num = 0

while True:
    try:
        user_input = input("Enter a number: ")
        num = float(user_input)
    except ValueError:
        print(f"Invalid! {user_input} may not be a number or it is a number list.")