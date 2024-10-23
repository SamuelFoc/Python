# Define the base class that all subclasses will inherit from
class BaseClass:
    def __new__(cls):
        # This method is called first when creating an instance of the class
        print(f"Creating instance of {cls.__name__} in BaseClass")
        # Calls the __new__ method of the parent class (object) to create a new instance
        return super().__new__(cls)

    def __init__(self):
        # This method initializes the instance created by __new__
        print(f"Initializing BaseClass")

    def greet(self):
        # A method in the base class that prints a message
        print("Hello from BaseClass")

# Define a subclass that inherits from BaseClass
class SubClass(BaseClass):
    def __new__(cls):
        # This method is called first when creating an instance of SubClass
        print(f"Creating instance of {cls.__name__} in SubClass")
        # Calls BaseClass.__new__() via super() to create an instance
        return super().__new__(cls)

    def __init__(self):
        # This method initializes the SubClass instance
        print(f"Initializing SubClass")
        # Calls BaseClass.__init__() to ensure the base class initialization is also performed
        super().__init__()

    def greet(self):
        # This method in SubClass overrides the greet method in BaseClass
        super().greet()  # Calls the greet method from BaseClass
        print("Hello from SubClass")  # Adds additional functionality

# Create an instance of SubClass
obj = SubClass()
# Call the greet method, which will use both BaseClass and SubClass methods
obj.greet()
