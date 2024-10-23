# Design Patterns in Python

This directory contains Python implementations of several key design patterns, including Factory, Builder, Strategy, Observer, Singleton, Decorator, Adapter, and Command patterns. Each design pattern solves specific software design problems and enhances the flexibility and maintainability of your code.

## Design Patterns Overview

### 1. **Factory Pattern**

The Factory Pattern provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

#### When to Use:

- When the exact type of objects to create is not known until runtime.
- When you want to decouple object creation from its implementation.

#### Advantages:

- Promotes loose coupling.
- Adds flexibility in introducing new types of products without modifying existing code.

#### Disadvantages:

- Can introduce complexity if overused.
- Might require subclassing, which can lead to rigid class hierarchies.

---

### 2. **Builder Pattern**

The Builder Pattern is used to construct complex objects step by step. It allows you to produce different types and representations of an object using the same construction code.

#### When to Use:

- When creating an object involves many steps or parameters.
- When you need to construct different representations of the same type of object.

#### Advantages:

- Separates the construction process from the representation.
- Facilitates the creation of immutable objects.
- Makes it easier to reuse and customize object creation.

#### Disadvantages:

- Might lead to too many small builder classes, increasing complexity.
- Requires familiarity with the pattern for developers to understand.

---

### 3. **Strategy Pattern**

The Strategy Pattern allows you to define a family of algorithms, encapsulate them in separate classes, and make them interchangeable.

#### When to Use:

- When you have different algorithms (strategies) that you want to swap in and out at runtime.
- When multiple classes differ only in their behavior.

#### Advantages:

- Provides flexibility in choosing algorithms at runtime.
- Reduces code duplication by centralizing common behavior in a single place.

#### Disadvantages:

- Increases the number of classes in your codebase.
- Clients must be aware of different strategy implementations.

---

### 4. **Observer Pattern**

The Observer Pattern defines a one-to-many relationship between objects, where one object (subject) updates its dependents (observers) automatically when its state changes.

#### When to Use:

- When one object's changes need to be reflected across multiple dependent objects.
- In event-driven systems, such as GUIs or real-time data updates.

#### Advantages:

- Promotes a loosely coupled system.
- Easier to add and remove observers dynamically.

#### Disadvantages:

- Observers may become complex and difficult to manage as the number of observers grows.
- Subjects and observers can have unexpected dependencies, making debugging harder.

---

### 5. **Singleton Pattern**

The Singleton Pattern ensures that a class has only one instance and provides a global point of access to it.

#### When to Use:

- When exactly one instance of a class is needed to coordinate actions across a system.
- In managing resources like database connections or thread pools.

#### Advantages:

- Controlled access to a single instance.
- Reduces memory footprint in scenarios where frequent creation of the same object occurs.

#### Disadvantages:

- Introduces a global state into the application, making it harder to test and maintain.
- Can lead to tight coupling and violations of the Single Responsibility Principle (SRP).

---

### 6. **Decorator Pattern**

The Decorator Pattern allows behavior to be added to individual objects, dynamically, without affecting the behavior of other objects from the same class.

#### When to Use:

- When you want to add responsibilities to objects without affecting other instances of the same class.
- When subclassing would result in too many subclasses to maintain.

#### Advantages:

- Offers flexibility in extending functionality at runtime.
- Promotes composition over inheritance.

#### Disadvantages:

- Can result in many small objects that are hard to manage.
- Makes debugging more challenging due to the layers of decorators.

---

### 7. **Adapter Pattern**

The Adapter Pattern allows incompatible interfaces to work together by providing a wrapper that translates one interface into another.

#### When to Use:

- When you need to integrate classes or systems that have incompatible interfaces.
- When you want to use a third-party library without modifying its code.

#### Advantages:

- Promotes reusability by allowing the integration of legacy code.
- Makes incompatible interfaces compatible without modifying existing code.

#### Disadvantages:

- Can introduce unnecessary complexity if not managed carefully.
- Increases the number of classes and objects.

---

### 8. **Command Pattern**

The Command Pattern encapsulates a request as an object, allowing you to parameterize methods with different requests, queue them, and support undoable operations.

#### When to Use:

- When you need to parameterize objects with operations.
- When you want to queue operations or implement undo/redo functionality.

#### Advantages:

- Decouples the invoker of the command from the receiver.
- Supports undo/redo operations easily.
- Can batch or queue commands for execution.

#### Disadvantages:

- Can result in an excessive number of command classes.
- May introduce additional complexity to the codebase.

---

## How to Run the Examples

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/design-patterns-python.git
   cd design-patterns-python
   ```

2. Each design pattern is located in its respective directory. To run the examples, navigate to the desired pattern's folder and run the Python script:

   ```bash
   cd Factory
   python factory_example.py
   ```

3. Repeat the steps for any other design patterns as needed.

## Conclusion

Each design pattern has specific use cases, advantages, and disadvantages. Understanding when and why to use them will improve your ability to design flexible, maintainable software systems. Use these patterns wisely, as they can greatly improve code reusability and separation of concerns, but overuse can lead to unnecessary complexity.
