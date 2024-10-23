# Concrete Coffee class (no abstract class)
class SimpleCoffee:
    def cost(self) -> float:
        return 5.0

    def description(self) -> str:
        return "Simple Coffee"

# Concrete Decorator - adds Milk (directly wraps coffee object)
class MilkDecorator:
    def __init__(self, coffee):
        self._decorated_coffee = coffee

    def cost(self) -> float:
        return self._decorated_coffee.cost() + 1.5

    def description(self) -> str:
        return self._decorated_coffee.description() + ", Milk"

# Concrete Decorator - adds Sugar (directly wraps coffee object)
class SugarDecorator:
    def __init__(self, coffee):
        self._decorated_coffee = coffee

    def cost(self) -> float:
        return self._decorated_coffee.cost() + 0.5

    def description(self) -> str:
        return self._decorated_coffee.description() + ", Sugar"

# Concrete Decorator - adds Vanilla (directly wraps coffee object)
class VanillaDecorator:
    def __init__(self, coffee):
        self._decorated_coffee = coffee

    def cost(self) -> float:
        return self._decorated_coffee.cost() + 2.0

    def description(self) -> str:
        return self._decorated_coffee.description() + ", Vanilla"

# Example usage
if __name__ == "__main__":
    # Start with a simple coffee
    coffee = SimpleCoffee()
    print(f"Cost: ${coffee.cost():.2f}, Description: {coffee.description()}")

    # Add milk
    coffee = MilkDecorator(coffee)
    print(f"Cost: ${coffee.cost():.2f}, Description: {coffee.description()}")

    # Add sugar
    coffee = SugarDecorator(coffee)
    print(f"Cost: ${coffee.cost():.2f}, Description: {coffee.description()}")

    # Add vanilla
    coffee = VanillaDecorator(coffee)
    print(f"Cost: ${coffee.cost():.2f}, Description: {coffee.description()}")
