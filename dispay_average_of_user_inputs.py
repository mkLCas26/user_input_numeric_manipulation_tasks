#  B4 Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

"""
Initialize empty list or needed variables
While loop for user input
    Try-except for determining invalid inputs
    Append user inputs in list
    Getting the average of the list
    Print the average
"""

numbers = []
num = 0
sum = 0

while True:
    user_input = input("\nEnter a number: ")
    try:
        num = float(user_input)
        numbers.append(num)
        
        for x in numbers:
            sum += x
            average = sum / len(numbers)
        print(f"The current average of your input is: {average}")
    except ValueError:
        print(f"Invalid! {user_input} may not be a number or it is a number list.")
        break