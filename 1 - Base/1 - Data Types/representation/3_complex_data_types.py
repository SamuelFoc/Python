import sys

# Function to retrieve and display information about Python data types/objects
def get_object_info(x, identifier: str = None):
    if identifier:  # If an identifier is provided, print it
        print(f"{identifier}\n---")
    print("Data Type:", type(x))  # Shows the type of the object
    print("Data ID:", id(x))  # Shows the memory address of the object
    print("Available Methods:", dir(x))  # Lists all available methods for the object
    print(f"Memory Size: {sys.getsizeof(x)} bytes")  # Displays the memory size of the object in bytes
    print("---\n")

# --- Test cases ---

# List
simple_list = [1, 2, 3, 4, 5]
nested_list = [1, [2, 3], [4, 5, 6]]  # A list with nested elements

# Set
simple_set = {1, 2, 3, 4, 5}
mixed_set = {1, "apple", 3.14, (1, 2)}  # A set with mixed types including a tuple

# Tuple
simple_tuple = (1, 2, 3)
nested_tuple = (1, (2, 3), (4, 5))  # A tuple with nested tuples

# Bytes
byte_data = b"Hello"
byte_array_data = bytes([65, 66, 67])  # Byte array representing ASCII codes for 'A', 'B', 'C'

# Dictionary
simple_dict = {"one": 1, "two": 2, "three": 3}
nested_dict = {"numbers": {"one": 1, "two": 2}, "letters": {"A": "Apple", "B": "Banana"}}  # Dictionary with nested dictionaries

# Calling the function with different objects
get_object_info(simple_list, "Simple List")
get_object_info(nested_list, "Nested List")
get_object_info(simple_set, "Simple Set")
get_object_info(mixed_set, "Mixed Set")
get_object_info(simple_tuple, "Simple Tuple")
get_object_info(nested_tuple, "Nested Tuple")
get_object_info(byte_data, "Byte Data")
get_object_info(byte_array_data, "Byte Array Data")
get_object_info(simple_dict, "Simple Dictionary")
get_object_info(nested_dict, "Nested Dictionary")
