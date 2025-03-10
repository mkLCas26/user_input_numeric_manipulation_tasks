# B3 Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

# Initialize counter and empty list
counter = 0
no_duplicate = []
duplicate = []

# While loop for user input
while counter < 10:
    counter += 1
    ten_numbers = int(input("Enter 10 numbers: "))

    # Determining if user input is already a part of the list
    if ten_numbers in no_duplicate:
        duplicate.append(ten_numbers)
    else:
        no_duplicate.append(ten_numbers) 

# Print numbers w/o duplicate
print(no_duplicate)