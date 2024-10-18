# Abstract Class Implementation in Python

## Overview

This repository demonstrates the implementation of abstract classes in Python using a custom `Abstract` class. Python, being a dynamically typed language, allows for flexible and powerful object-oriented programming. Abstract classes serve as blueprints for other classes, enabling a consistent interface while enforcing method implementation in subclasses.

## Abstract Class

The `Abstract` class provides a decorator `abstractmethod`, which can be used to mark methods as abstract. When a method is decorated with `@abstractmethod`, any attempt to call that method directly on an instance of the abstract class will raise a `NotImplementedError`, ensuring that subclasses provide their own implementations.

### Example: Vehicle and Car

In this example, we create an abstract `Vehicle` class and a concrete `Car` subclass that implements the abstract methods.

#### Abstract Class Definition

```python
class Abstract:
    """Base class for all abstract classes providing an abstract method decorator."""

    @staticmethod
    def abstractmethod(method):
        """Decorator to mark a method as abstract."""
        def wrapper(*args, **kwargs):
            raise NotImplementedError(f"The method '{method.__name__}' must be implemented in the subclass.")

        wrapper.__name__ = method.__name__  # Preserve the original method name
        wrapper.__doc__ = method.__doc__      # Preserve the original docstring
        return wrapper
```

#### Vehicle Class

```python
class Vehicle(Abstract):
    """Abstract base class for all vehicles."""

    def __init__(self, v_type, weight):
        self.v_type = v_type
        self.weight = weight

    @Abstract.abstractmethod
    def ride(self):
        """Method to be implemented in subclasses to ride the vehicle."""
        pass
```

#### Car Class Implementation

```python
class Car(Vehicle):
    def __init__(self, v_type, weight, passengers):
        super().__init__(v_type, weight)
        self._passengers = passengers

    def ride(self):
        print("I am riding a car..")
```

#### Usage Example

To use the `Car` class:

```python
# Creating a car object
car = Car("Car", 5)
car.ride()  # Output: I am riding a car..
```

### Key Features

- **Abstract Method Enforcement**: By using the `abstractmethod` decorator, we ensure that all subclasses of `Vehicle` implement the `ride` method. If they do not, attempting to call `ride` on a `Vehicle` instance will raise an error.
- **Dynamic Typing**: Python's dynamic nature allows for flexibility in defining and using abstract classes without rigid type constraints, making it easier to work with different types of subclasses.

## Conclusion

This implementation demonstrates how Python can effectively manage abstract classes, enabling developers to create robust and flexible object-oriented designs. By enforcing method implementation in subclasses, we can ensure a consistent interface across different types of vehicles.
