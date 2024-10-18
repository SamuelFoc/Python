# 1. Standard Function Definition
def add(a, b):
    return a + b

result = add(3, 5)
print("Standard Function Result:", result)  # Output: 8


# 2. Default Parameter Values
def greet(name="World"):
    return f"Hello, {name}!"

print("Greet with default:", greet())          # Output: Hello, World!
print("Greet with parameter:", greet("Alice"))  # Output: Hello, Alice!


# 3. Variable-Length Arguments
def add_multiple(*args):
    return sum(args)

print("Sum of multiple numbers:", add_multiple(1, 2, 3, 4))  # Output: 10


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("Print Info:")
print_info(name="Alice", age=30)  
# Output: 
# name: Alice
# age: 30


# 4. Lambda Functions
square = lambda x: x * x
print("Lambda Function Result:", square(5))  # Output: 25

# Using with map
numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x * x, numbers))
print("Squared Numbers:", squared_numbers)  # Output: [1, 4, 9, 16]


# 5. Nested Functions
def outer_function(message):
    def inner_function():
        return message
    return inner_function()

print("Nested Function Result:", outer_function("Hello, World!"))  # Output: Hello, World!
