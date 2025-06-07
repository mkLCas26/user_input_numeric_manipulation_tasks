# B2 Prog07: Ask 10 user number inputs. Print how many are even numbers.

# Initialize counter and empty list
counter = 0
even_numbers = []

# While loop for user input
while counter < 10:
    ten_numbers = int(input(f"Enter number {counter + 1}/10: "))
    counter += 1
    
    # Determining even numbers
    if ten_numbers % 2 == 0:
        even_numbers.append(ten_numbers)

# Print length of even numbers
print(len(even_numbers))