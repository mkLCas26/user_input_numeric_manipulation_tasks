# B2 Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

# First user input, initialize counter and other variables
first_input = int(input("Enter number 1/10: "))
counter = 1

# While loop for user input and difference
while counter < 10:
    other_inputs = int(input(f"Enter number {counter + 1}/10: "))
    counter += 1

    first_input -= other_inputs

# Print difference
print(first_input)