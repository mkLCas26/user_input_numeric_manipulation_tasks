# B4 Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.
 
"""
Initialize empty lists or needed variables
while loop for user input
    Try-except for determining invalid inputs
    Determining most duplicates from user input
    Print number with most duplicate
"""

numbers = []
num = 0
max_dupli = 0
freq_num = 0
counter = 0

while True:
    user_input = input("\nEnter a number: ")
    try: 
        num = float(user_input)
        numbers.append(num)

        for x in numbers:
            num_count = numbers.count(x)
            if num_count > max_dupli:
                max_dupli = num_count
                freq_num = x
        print(f"{freq_num} has the most duplicates. Duplicate Count: {max_dupli} ")

    except ValueError:
        print(f"Invalid! {user_input} may not be a number or it is a number list.")
        break



    


