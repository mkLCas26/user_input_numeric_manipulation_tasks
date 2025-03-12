# B3 Prog01: Ask 10 user number inputs. Print numbers with no duplicate.

# Initialize counter and empty list
counter = 0
numbers = []
no_duplicate = []

# While loop for user input
while counter < 10:
    user_num = int(input(f"Enter number {counter + 1}/10: "))
    numbers.append(user_num)
    counter += 1

# Determining if user input is already a part of the list
for x in numbers:
    if numbers.count(x) == 1:
        no_duplicate.append(x)

# Print numbers w/o duplicate
print(no_duplicate)