from Vehicle.Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, v_type, weight, passengers):
        super().__init__(v_type, weight)
        self._passengers = passengers

    def print(self):
        super().print()
        print(f"Seats: {self._passengers}")

    def ride(self):
        print("I am riding a car..")