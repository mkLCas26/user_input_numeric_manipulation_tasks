# B3 Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

"""
Initialize empty list or variables needed
While loop for user input
    Try-except for determining invalid inputs
    Storing number inputs in a list
    Use sort() function for printing list in ascending order
    Print sorted list
"""

numbers = []
num = 0

while True: 
    try:
        user_input = input("Enter a number: ")
        num = float(user_input)
        numbers.append(num)
        numbers.sort()
        print(numbers)

    except ValueError:
        print(f"Invalid! {user_input} may not be a number or it is a number list.")
        break