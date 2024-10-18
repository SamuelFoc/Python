# Function Definitions in Python

Functions are a fundamental aspect of Python programming, allowing for code reusability and organization. This guide covers the first five types of function definitions in Python.

## 1. Standard Function Definition

Standard functions are defined using the `def` keyword, followed by the function name and parentheses that can include parameters. They can perform tasks and return values.

### Syntax:

```python
def function_name(parameters):
    # Code block
    return value
```

### Example:

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8
```

## 2. Default Parameter Values

Functions can have default values for parameters, making them optional. If the caller does not provide a value for that parameter, the default value is used.

### Example:

```python
def greet(name="World"):
    return f"Hello, {name}!"

print(greet())          # Output: Hello, World!
print(greet("Alice"))  # Output: Hello, Alice!
```

## 3. Variable-Length Arguments

Python allows you to define functions that accept a variable number of arguments using `*args` for non-keyword arguments and `**kwargs` for keyword arguments.

### Example with `*args`:

```python
def add_multiple(*args):
    return sum(args)

print(add_multiple(1, 2, 3, 4))  # Output: 10
```

### Example with `**kwargs`:

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30)
# Output:
# name: Alice
# age: 30
```

## 4. Lambda Functions

Lambda functions are small anonymous functions defined with the `lambda` keyword. They can take any number of arguments but can only have one expression. They are commonly used for short operations, especially in functional programming.

### Syntax:

```python
lambda arguments: expression
```

### Example:

```python
square = lambda x: x * x
print(square(5))  # Output: 25

# Using with map
numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16]
```

## 5. Nested Functions

Nested functions are defined within other functions. The inner function can access variables from the outer function, providing a way to encapsulate functionality.

### Example:

```python
def outer_function(message):
    def inner_function():
        return message
    return inner_function()

print(outer_function("Hello, World!"))  # Output: Hello, World!
```

---

These five types of function definitions in Python provide flexibility and allow you to write clean, efficient, and reusable code. Understanding these concepts will greatly enhance your programming skills and code organization.
