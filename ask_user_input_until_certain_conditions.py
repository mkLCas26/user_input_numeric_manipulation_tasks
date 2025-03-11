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
num = 0


while True:
    user_input = (input("\nEnter a number: "))

    try: 
        num = float(user_input)
        print("try, valid!")
    except ValueError:
        print(f"Invalid! {user_input} is not a number. ")
        break    
