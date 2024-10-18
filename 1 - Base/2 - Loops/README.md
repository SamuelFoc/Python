# Loops in Python

Loops are fundamental programming constructs that allow you to execute a block of code repeatedly. In Python, there are two main types of loops: `for` loops and `while` loops. This guide will introduce you to each type, along with their uses and features.

## 1. `for` Loop

The `for` loop is used to iterate over a sequence (such as a list, tuple, string, dictionary, or range). It allows you to execute a block of code for each element in the sequence.

### Syntax:

```python
for element in sequence:
    # Block of code
```

### Example:

```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)  # Outputs: 1, 2, 3, 4, 5
```

### Key Features:

- Iterates over items in a sequence.
- Use `range()` to generate a sequence of numbers.

```python
for i in range(5):
    print(i)  # Outputs: 0, 1, 2, 3, 4
```

---

## 2. `while` Loop

The `while` loop repeatedly executes a block of code as long as a specified condition is true.

### Syntax:

```python
while condition:
    # Block of code
```

### Example:

```python
count = 0
while count < 5:
    print(count)
    count += 1  # Outputs: 0, 1, 2, 3, 4
```

### Key Features:

- The loop continues until the condition becomes `False`.
- Avoid infinite loops by ensuring the condition will eventually be met.

---

## 3. Nested Loops

You can nest loops inside one another. This is useful for iterating over multidimensional data structures.

### Example:

```python
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
```

### Output:

```
i: 0, j: 0
i: 0, j: 1
i: 1, j: 0
i: 1, j: 1
i: 2, j: 0
i: 2, j: 1
```

---

## 4. Control Statements: `break` and `continue`

### `break`

- Exits the loop prematurely when a specified condition is met.

### Example:

```python
for i in range(10):
    if i == 5:
        break  # Exit the loop when i equals 5
    print(i)  # Outputs: 0, 1, 2, 3, 4
```

### `continue`

- Skips the rest of the loop for the current iteration and moves to the next iteration.

### Example:

```python
for i in range(5):
    if i == 2:
        continue  # Skip the current iteration when i equals 2
    print(i)  # Outputs: 0, 1, 3, 4
```

---

## 5. `else` Clause with Loops

Python allows an `else` clause to be used with loops. The `else` block is executed after the loop finishes, unless the loop is terminated with a `break` statement.

### Example:

```python
for i in range(5):
    print(i)
else:
    print("Loop finished")  # This will always execute after the loop
```

### Example with `break`:

```python
for i in range(5):
    if i == 3:
        break
else:
    print("This will not be printed because the loop was terminated early")
```

---

## Summary

- **`for` Loop**: Iterates over a sequence.
- **`while` Loop**: Repeats while a condition is true.
- **Nested Loops**: Loops within loops for multidimensional iteration.
- **Control Statements**: Use `break` to exit and `continue` to skip iterations.
- **`else` with Loops**: Executes if the loop completes normally.

Understanding these loop constructs will enable you to efficiently perform repetitive tasks and manipulate collections of data in Python.

---

Feel free to print or share this guide as needed!
