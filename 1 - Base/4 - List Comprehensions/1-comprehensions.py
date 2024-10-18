# Original list of integers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Create a list of squares of even numbers
squares_of_evens = [x**2 for x in numbers if x % 2 == 0]

# 2. Create a list of strings representing whether the numbers are even or odd
even_odd_strings = [f"{x} is {'even' if x % 2 == 0 else 'odd'}" for x in numbers]

# 3. Create a list of only the odd numbers
odd_numbers = [x for x in numbers if x % 2 != 0]

# Print the results
print("Original numbers:", numbers)
print("Squares of even numbers:", squares_of_evens)
print("Even/Odd strings:", even_odd_strings)
print("Odd numbers:", odd_numbers)