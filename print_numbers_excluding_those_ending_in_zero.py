# B1 Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

# Initialize empty list
no_zero = []

# For loop to print numbers from 0-100
for x in range(0, 100):
    if x % 10 != 0:         # Determine numbers not ending in zero to exclude those that end in zero
        no_zero.append(x)
# Print list
print(no_zero)