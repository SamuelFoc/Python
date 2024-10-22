from abc import ABC, abstractmethod

# Abstract base class representing a general car. 
# It defines the interface for all car types.
class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

# Concrete implementation of a Sedan car. 
# This class provides the specific behavior 
# for driving a Sedan.
class Sedan(Car):
    def drive(self):
        return "Driving a Sedan!"

# Concrete implementation of an SUV car. 
# This class provides the specific behavior 
# for driving an SUV.
class SUV(Car):
    def drive(self):
        return "Driving an SUV!"

# Factory class responsible for creating
# instances of cars based on the specified type.
class CarFactory:
    @staticmethod
    def create_car(car_type: str) -> Car:
        if car_type == "sedan":
            return Sedan()
        elif car_type == "suv":
            return SUV()
        else:
            raise ValueError(f"Unknown car type: {car_type}")

if __name__ == "__main__":
    factory = CarFactory()

    # Create a Sedan car and drive it.
    sedan = factory.create_car("sedan")
    print(sedan.drive())

    # Create an SUV car and drive it.
    suv = factory.create_car("suv")
    print(suv.drive())

    # Attempt to create a car with an unknown type, 
    # which raises a ValueError.
    try:
        unknown_car = factory.create_car("truck")
    except ValueError as e:
        print(e)
