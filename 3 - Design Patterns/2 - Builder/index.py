# Car class representing a general car with attributes like make, model, year, and type.
class Car:
    def __init__(self, make: str, model: str, year: int, car_type: str):
        self.make = make
        self.model = model
        self.year = year
        self.car_type = car_type

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.car_type})"

# Builder class for constructing Car objects step by step.
class CarBuilder:
    def __init__(self):
        self.make = ""
        self.model = ""
        self.year = 0
        self.car_type = ""

    # Method to set the make of the car.
    def set_make(self, make: str):
        self.make = make
        return self  # Return self for chaining.

    # Method to set the model of the car.
    def set_model(self, model: str):
        self.model = model
        return self  # Return self for chaining.

    # Method to set the year of the car.
    def set_year(self, year: int):
        self.year = year
        return self  # Return self for chaining.

    # Method to set the type of the car.
    def set_car_type(self, car_type: str):
        self.car_type = car_type
        return self  # Return self for chaining.

    # Method to build the Car object using the provided attributes.
    def build(self) -> Car:
        return Car(self.make, self.model, self.year, self.car_type)

# Example usage of the Builder pattern to create different types of cars.
if __name__ == "__main__":
    # Create a Sedan using the builder pattern
    sedan_builder = CarBuilder()
    sedan = (sedan_builder
             .set_make("Toyota")
             .set_model("Camry")
             .set_year(2023)
             .set_car_type("Sedan")
             .build())
    print(sedan)

    # Create an SUV using the builder pattern
    suv_builder = CarBuilder()
    suv = (suv_builder
           .set_make("Ford")
           .set_model("Explorer")
           .set_year(2022)
           .set_car_type("SUV")
           .build())
    print(suv)

    # Example of creating a car with different specifications
    custom_car = (CarBuilder()
                  .set_make("Tesla")
                  .set_model("Model X")
                  .set_year(2024)
                  .set_car_type("SUV")
                  .build())
    print(custom_car)