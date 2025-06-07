# B4 Prog04: Ask user number input until invalid. 
# Print input in ascending order. Use sort()

"""
PSEUDOCODE
Initialize empty lists or needed variables
While loop for user input
    Try-except for determining invalid inputs
    Storing number inputs in a list
    Use sort() function for the descending order
    Print list of number inputs in descending order
"""

numbers = []
num = 0

while True:
    user_input = input("Enter a number: ")
    try:
        num = float(user_input)
        numbers.append(num)
        numbers.sort(reverse=True)
        print(numbers)
        
    except ValueError:
        print(f"Invalid! {user_input} may not be a number or it is a number list.")