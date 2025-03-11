# B3 Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

# Initialize counter and empty list
counter = 0
duplicate_once = []

# While loop for user input
while counter < 10:
    user_input = int(input(f"Enter number {counter + 1}/10: "))
    counter += 1

    # Determining duplicate and printing it once
    if user_input in duplicate_once:
        duplicate_once.remove(user_input)

# Print final list of numbers
print(duplicate_once)