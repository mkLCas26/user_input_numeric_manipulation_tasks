# B3 Prog02: Ask 10 user number inputs. Display all numbers. 
# For numbers with duplicate, display only the first entry.

# Initialize counter and empty list
counter = 0
numbers = []
duplicate_once = []

# While loop for user input
while counter < 10:
    user_input = int(input(f"Enter number {counter + 1}/10: "))
    counter += 1

    # Determining duplicate and printing it once
    if user_input in duplicate_once:
        numbers.append(user_input)
    else: 
        duplicate_once.append(user_input)

# Print final list of numbers
print(duplicate_once)