import sys

# Define an integer
x = 10

# Display information about the integer
print("Data Type:", type(x))  # Shows the type of the variable
print("Data ID:", id(x))  # Shows the memory address of the variable
print("Available Methods:", dir(x))  # Lists all available methods for the integer
print(f"Memory Size: {sys.getsizeof(x)} bytes")  # Displays the memory size of the variable in bytes
