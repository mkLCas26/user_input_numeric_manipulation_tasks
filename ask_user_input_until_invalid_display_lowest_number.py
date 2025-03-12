# B3 Prog04: Ask user number input until invalid. Print lowest number.

"""
Initialize empty list and needed variable
While loop for user input
    Try-except for invalid inputs
    Determining the lowest number using if-else
    Displaying the lowest number
"""

lowest = None
num = 0

while True: 
    user_input = input("\nEnter a number: ")

    try:
        num = float(user_input)

        if lowest == None:
            lowest = num
        elif num < lowest:
            lowest = num
        
        print(f"Lowest Number: {lowest}")

    except ValueError:
        print(f"Invalid! {user_input} may not be a number or it is a number list.")
        break