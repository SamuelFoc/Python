# Iterators

An iterator is a fundamental concept in Python that allows you to iterate (or loop) over collections like lists, tuples, dictionaries, or custom objects. In Python, an iterator is an object that can be traversed through all of its elements, one at a time.

### Key Concepts:

1. **Iterable**: Any Python object that can return an iterator (like lists, tuples, sets, etc.) is called an _iterable_. It implements the `__iter__()` method, which returns an iterator.
2. **Iterator**: An iterator is an object with a state so that it remembers where it is during iteration. It must implement two methods:
   - `__iter__()`: Returns the iterator object itself. This is required so that the object can be used in loops like `for`.
   - `__next__()`: Returns the next element in the sequence. When there are no more elements to return, it raises a `StopIteration` exception, which signals the end of the iteration.

### How Iterators Work:

- **Behind a `for` loop**: When you use a `for` loop on an iterable, Python internally calls `iter()` to get an iterator and then repeatedly calls `next()` on that iterator until `StopIteration` is raised.

#### Example of a Simple Iterator:

Let’s create a custom iterator that returns numbers from 1 to 5:

```python
class SimpleIterator:
    def __init__(self):
        self.current = 1

    # __iter__ returns the iterator object itself
    def __iter__(self):
        return self

    # __next__ returns the next item
    def __next__(self):
        if self.current <= 5:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration  # End of iteration

# Using the iterator
simple_iter = SimpleIterator()

# Manually iterating using the next() function
print(next(simple_iter))  # Output: 1
print(next(simple_iter))  # Output: 2
print(next(simple_iter))  # Output: 3
print(next(simple_iter))  # Output: 4
print(next(simple_iter))  # Output: 5
# After 5, StopIteration will be raised if we call next() again.
```

### Iterators vs Iterables:

- **Iterable**: Any object capable of returning an iterator (it implements `__iter__()`), like lists, tuples, and dictionaries.
- **Iterator**: The object that keeps state of where it is during iteration (it implements both `__iter__()` and `__next__()`).

For example:

```python
# Lists are iterables, and you can obtain an iterator from them:
my_list = [1, 2, 3]
my_iter = iter(my_list)  # my_iter is now an iterator

# Manually retrieve elements using next()
print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3
# StopIteration will be raised if you call next() again
```

### Generators as Iterators:

In Python, **generators** are a simpler way to create iterators. You define a function with `yield` statements, and when you call it, it returns a generator object, which is an iterator. Each call to `next()` will execute the function until it hits a `yield`.

Here’s an example of using a generator (like the one from your original code):

```python
def number_generator():
    for i in range(1, 6):
        yield i

gen = number_generator()

# Using next() to iterate through the generator
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
print(next(gen))  # Output: 4
print(next(gen))  # Output: 5
# After 5, StopIteration will be raised
```

### Iterator Protocol:

To summarize, the **iterator protocol** in Python consists of:

1. **`__iter__()`**: Returns the iterator object itself.
2. **`__next__()`**: Returns the next value in the iteration, or raises `StopIteration` if no more items are available.

### Practical Use of Iterators:

Iterators are powerful for dealing with:

- **Lazy evaluation**: Only computing elements as needed (e.g., reading large files line by line, which you implemented in your original code).
- **Infinite sequences**: You can define iterators that generate infinite numbers or values until a specific condition is met.

#### Infinite Iterator Example:

Here’s a basic example of an infinite iterator that keeps yielding numbers indefinitely:

```python
class InfiniteNumbers:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        return self.num

# Usage
inf_iter = InfiniteNumbers()
print(next(inf_iter))  # Output: 1
print(next(inf_iter))  # Output: 2
# It can keep going indefinitely
```

Would you like to explore any specific aspect of iterators or work with a practical use case?
