# B3 Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

"""
Initializing empty lists and needed variables
Initial user input
While loop for user input 
    Use try to check if use input is a number
    Determining whether to display "Unique" and "Duplicate"

"""

numbers = []
duplicate = []


try: 
    user_input = float(input("Enter a number: "))
    print("tama")
except ValueError:
    print(f"Invalid! {user_input} is not a number. ")    



