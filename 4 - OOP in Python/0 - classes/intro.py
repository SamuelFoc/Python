# Define a basic class MyClass without explicit inheritance
class MyClass:
    def __new__(cls):
        # This method is called to create a new instance of the class
        print(f"Creating instance of {cls.__name__}")
        # super().__new__(cls) calls the __new__ method of the parent class (object)
        instance = super().__new__(cls)  # Creates a new instance of MyClass
        return instance  # Return the new instance

    def __init__(self):
        # __init__ initializes the instance after it's created
        print(f"Initializing instance of {self.__class__.__name__}")

# Create an instance of MyClass
obj = MyClass()