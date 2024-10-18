from Abstract.Abstract import Abstract 

class Vehicle(Abstract):
    def __init__(self, v_type, weight):
        self._v_type = v_type
        self._weight = weight

    def print(self):
        print(f"\n---\nType: {self._v_type}\nWeight:{self._weight}")

    @Abstract.abstractmethod
    def ride(self):
        pass