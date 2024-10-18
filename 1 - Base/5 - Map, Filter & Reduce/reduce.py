# Import the reduce function from the functools module
from functools import reduce

# Define a function to multiply two numbers
def multiply(x, y):
    return x * y

# List of integers
numbers = [1, 2, 3, 4, 5]

# Use reduce to calculate the product of all numbers in the list
product = reduce(multiply, numbers)

# Print the result
print("Original Numbers:", numbers)
print("Product of Numbers:", product)
