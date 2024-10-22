from abc import ABC, abstractmethod

# Strategy interface for driving behavior
class DrivingStrategy(ABC):
    @abstractmethod
    def drive(self):
        pass

# Concrete strategy for economy driving
class EconomyDrivingStrategy(DrivingStrategy):
    def drive(self):
        return "Driving economically, saving fuel!"

# Concrete strategy for sport driving
class SportDrivingStrategy(DrivingStrategy):
    def drive(self):
        return "Driving sportily, enjoying the speed!"

# Concrete strategy for off-road driving
class OffRoadDrivingStrategy(DrivingStrategy):
    def drive(self):
        return "Driving off-road, tackling tough terrains!"

# Context class that uses the strategy
class Car:
    def __init__(self, make: str, model: str, strategy: DrivingStrategy):
        self.make = make
        self.model = model
        self.strategy = strategy

    def set_driving_strategy(self, strategy: DrivingStrategy):
        self.strategy = strategy

    def drive(self):
        return self.strategy.drive()

# Example usage of the Strategy pattern
if __name__ == "__main__":
    # Create a car with economy driving strategy
    economy_car = Car("Toyota", "Prius", EconomyDrivingStrategy())
    print(f"{economy_car.make} {economy_car.model}: {economy_car.drive()}")

    # Change to sport driving strategy
    economy_car.set_driving_strategy(SportDrivingStrategy())
    print(f"{economy_car.make} {economy_car.model}: {economy_car.drive()}")

    # Create a car with off-road driving strategy
    offroad_car = Car("Jeep", "Wrangler", OffRoadDrivingStrategy())
    print(f"{offroad_car.make} {offroad_car.model}: {offroad_car.drive()}")
