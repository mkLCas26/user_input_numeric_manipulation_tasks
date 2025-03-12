# B4 Prog03: Ask user number input until invalid. Print highest number.

"""
PSEUDOCODE
Initialize empty list or needed variables
While loop for user input
    Try-except to determine invalid inputs
    Determine highest number using if-else
    Print the highest number
"""

highest = None
num = 0

while True:
    user_input = input("\nEnter a number: ")
    try:
        num = float(user_input)

        if highest == None:
            highest = num
        elif num > highest:
            highest = num   
        print(f"Highest Number: {highest}")

    except ValueError:
        print(f"Invalid! {user_input} may not be a number or it is a number list.")
        break