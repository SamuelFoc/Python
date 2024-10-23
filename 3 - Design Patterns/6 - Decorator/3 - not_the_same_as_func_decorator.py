# Base Coffee class
class SimpleCoffee:
    def cost(self) -> float:
        return 5.0

    def description(self) -> str:
        return "Simple Coffee"

# Function decorators (using @ syntax) to wrap methods
def add_milk(coffee_method):
    def wrapper(self):
        cost = coffee_method(self) + 1.5  # Add milk cost
        return cost
    return wrapper

def add_sugar(coffee_method):
    def wrapper(self):
        cost = coffee_method(self) + 0.5  # Add sugar cost
        return cost
    return wrapper

# Coffee class with decorators applied
class CoffeeWithAddOns(SimpleCoffee):

    # Apply add_milk decorator first, then apply add_sugar
    @add_sugar
    @add_milk
    def cost(self) -> float:
        return super().cost()  # Get the original coffee cost

    def description(self) -> str:
        return super().description() + ", Milk, Sugar"

# Example usage
if __name__ == "__main__":
    coffee = CoffeeWithAddOns()
    print(f"Cost: ${coffee.cost():.2f}, Description: {coffee.description()}")
