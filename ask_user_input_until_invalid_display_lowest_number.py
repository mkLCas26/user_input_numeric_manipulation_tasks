# B3 Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

"""
Initialize empty list and needed variable
While loop for user input
    Try-except for invalid inputs
    Determining the lowest number in the list
    Displaying the lowest number
"""

numbers = []
num = 0

while True: 
    user_input = input("\nEnter a number: ")

    try:
        num = float(user_input)
        numbers.append(num)

        for x in numbers:
            if x > num:
                print(num)
            else: 
                print(x)

    except ValueError:
        print(f"Invalid! {user_input} may not be a number or it is a number list.")
        break 