# B1 Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

# Initialize Counter and other variables
counter = 0
sum = 0

# While Loop for 10 user inputs and sum
while counter < 10:
    ten_numbers = int(input(f"Enter number {counter + 1}/10: ")) 
    counter += 1

    sum += ten_numbers

# Print sum
print(sum)