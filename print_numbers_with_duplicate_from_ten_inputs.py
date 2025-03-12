# B4 Prog01: Ask 10 user number inputs. Print numbers with duplicate.

"""
Initialize empty lists and needed variables
While loop for 10 user inputs 
    Append input in list
For loop for determining if number is a duplicate
Printing numbers with duplicate
"""

counter = 0
duplicate = []
numbers = []

while counter < 10:
    user_input = int(input(f"Enter number {counter +1}/10: "))
    numbers.append(user_input)
    counter += 1

for x in numbers:
    if numbers.count(x) > 1 and x not in duplicate:
        duplicate.append(x)
    

print(duplicate)

