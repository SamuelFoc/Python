# Iterable data types in Python

# 1. Lists
print("Iterating over a list:")
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

print("\n")  # New line for better readability

# 2. Tuples
print("Iterating over a tuple:")
my_tuple = (1, 2, 3, 4, 5)
for item in my_tuple:
    print(item)

print("\n")  # New line for better readability

# 3. Sets
print("Iterating over a set:")
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)

print("\n")  # New line for better readability

# 4. Dictionaries
print("Iterating over a dictionary:")
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Iterate over keys
print("Keys:")
for key in my_dict:
    print(key)

# Iterate over values
print("\nValues:")
for value in my_dict.values():
    print(value)

# Iterate over key-value pairs
print("\nKey-Value Pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

print("\n")  # New line for better readability

# 5. Strings
print("Iterating over a string:")
my_string = "Hello"
for char in my_string:
    print(char)

print("\n")  # New line for better readability

# 6. Ranges
print("Iterating over a range:")
for num in range(5):  # Generates numbers from 0 to 4
    print(num)

print("\n")  # New line for better readability

# 7. Files
# Note: This part of the code requires an actual file to read.
# Please create a file named 'example.txt' with some text content before running this part.

try:
    with open('example.txt', 'r') as file:
        print("Iterating over a file:")
        for line in file:
            print(line.strip())  # Print each line without leading/trailing whitespace
except FileNotFoundError:
    print("File 'example.txt' not found. Please create the file to see this part in action.")


#! There are also a custom iterable objects that you can create using classes !
#! See the "Generators Iterators" folder