# Initialize a list of integers from 1 to 10
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# First loop: Iterates through each number in the array
for number in arr:
    # Print the current iteration number
    print(f"Iteration: {number}")

# Second loop: Iterates from 0 to 10 (inclusive)
for number in range(11):
    # Print the current iteration number
    print(f"Iteration: {number}")

# Third loop: Checks each number in the array to categorize it
for number in arr:
    if number < 5:  # Condition to check if the number is less than 5
        # If the number is less than 5, print this message
        print("Less than 5")
    else:  # If the number is 5 or greater
        # If the number is 5 or greater, print this message
        print("Greater than 5")

# Fourth loop: Only prints numbers greater than or equal to 5
for number in arr:
    if number < 5:  # Condition to check if the number is less than 5
        continue  # Skip the current iteration if the number is less than 5
    else:  # If the number is 5 or greater
        # Print that the number is greater than or equal to 5
        print("Greater than 5")

# Fifth loop: Prints numbers until it encounters the number 6
for number in arr:
    if number == 6:  # Check if the number is 6
        break  # Exit the loop if the number is 6
    else:  # If the number is not 6
        # Print that the loop is currently processing this number
        print(f"Looping.. {number}")
