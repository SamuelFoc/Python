# Define a function to check if a number is even
def is_even(num):
    return num % 2 == 0

# List of integers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter to get only even numbers from the list
even_numbers = list(filter(is_even, numbers))

# Print the results
print("Original Numbers:", numbers)
print("Even Numbers:", even_numbers)
