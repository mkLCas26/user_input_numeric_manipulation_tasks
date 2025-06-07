# B3 Prog03: Ask user number input until invalid. 
# Print "Unique" if it has no duplicate
# Print "Duplicate" if it is a duplicate

"""
PSEUDOCODE
Initializing empty lists and needed variables
While loop for user input 
    Use try to check if use input is a number
    Determining whether to display "Unique" and "Duplicate"
        Unique if no dupe and Duplicate if may dupe
"""

numbers = []
duplicate = []
num = 0


while True:
    user_input = (input("\nEnter a number: "))

    try: 
        num = float(user_input)

        if num in numbers:
            duplicate.append(num)
            print("Duplicate")
        else: 
            numbers.append(num)
            print("Unique") 

    except ValueError:
        print(f"Invalid! {user_input} may not be a number or it is a number list. ")
        break    
