import sys

# Function to retrieve and display information about Python data types/objects
def get_object_info(x, identifier: str = None):
    if identifier:  # If an identifier is provided, print it
        print(f"{identifier}\n---")
    print("Data Type:", type(x))  # Shows the type of the object
    print("Data Address (HEX):", hex(id(x)))  # Shows the memory address of the object
    print("Available Methods:", dir(x))  # Lists all available methods for the object
    print(f"Memory Size: {sys.getsizeof(x)} bytes")  # Displays the memory size of the object in bytes
    print("---\n")

# --- Test cases ---

# Integer Numbers
int_num = 10
large_int_num = 1000  # A larger integer

# Floating Point Numbers
float_num = 3.14
precise_float_num = 2.718281828459045235360287471352  # High-precision float

# Rational Number (Result of Division)
rational_num = 1 / 3

# Large Integer (Tera integer)
tera_int_num = 10**12  # Large integer (10^12)

# Complex Numbers
complex_num = 3 + 4j
complex_num_precise = 2.5 + 6.8j  # A complex number with more precise float components

# Boolean Values
bool_true = True
bool_false = False

# Strings
simple_string = "Hello, World!"
long_string = "This is a longer string example for testing."

# Calling the function with different objects
get_object_info(int_num, "Integer")
get_object_info(large_int_num, "Large Integer")
get_object_info(float_num, "Float")
get_object_info(precise_float_num, "Precise Float")
get_object_info(rational_num, "Rational Number")
get_object_info(tera_int_num, "Tera Integer")
get_object_info(complex_num, "Complex Number")
get_object_info(complex_num_precise, "Precise Complex Number")
get_object_info(bool_true, "Boolean (True)")
get_object_info(bool_false, "Boolean (False)")
get_object_info(simple_string, "String")
get_object_info(long_string, "Long String")
