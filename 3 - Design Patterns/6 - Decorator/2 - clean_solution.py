from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

class SimpleCoffee(Coffee):
    def cost(self) -> float:
        return 5.0
    
    def description(self) -> str:
        return "Simple Coffe"
    
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._decorated_coffee = coffee

    def cost(self) -> float:
        return self._decorated_coffee.cost()
    
    def description(self) -> str:
        return self._decorated_coffee.description()
    
class MilkDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._decorated_coffee.cost() + 1.5
    
    def description(self) -> str:
        return self._decorated_coffee.description() + ", Milk"
    
class SugarDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._decorated_coffee.cost() + 0.5
    
    def description(self) -> str:
        return self._decorated_coffee.description() + ", Sugar"
    
class VanillaDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._decorated_coffee.cost() + 2.0
    
    def description(self) -> str:
        return self._decorated_coffee.description() + ", Vanilla"
    
