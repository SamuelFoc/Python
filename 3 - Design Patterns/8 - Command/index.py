from abc import ABC, abstractmethod

class CoffeeCommand(ABC):
    @abstractmethod
    def execute(self):
        pass


class Barista:
    def brew_espresso(self):
        print("Brewing an Espresso..")

    def brew_cappuccino(self):
        print("Brewing Capuccino..")

    def brew_latte(self):
        print("Brewing a Latte..")

class BrewEspressoCommand(CoffeeCommand):
    def __init__(self, barista: Barista):
        self.barista = barista

    def execute(self):
        self.barista.brew_espresso()

class BrewCappuccinoCommand(CoffeeCommand):
    def __init__(self, barista: Barista):
        self.barista = barista

    def execute(self):
        return self.barista.brew_cappuccino()
    
class BrewLatteCommand(CoffeeCommand):
    def __init__(self, barista: Barista):
        self.barista = barista

    def execute(self):
        return self.barista.brew_latte()
    
class CoffeeShop:
    def __init__(self):
        self.orders = []

    def take_order(self, command: CoffeeCommand):
        self.orders.append(command)

    def serve_orders(self):
        for order in self.orders:
            order.execute()
        self.orders.clear()


# Example usage
if __name__ == "__main__":
    # The barista (receiver)
    barista = Barista()

    # CoffeeShop is the Invoker, and it takes commands (orders)
    coffee_shop = CoffeeShop()

    # Creating some coffee orders (commands)
    espresso_order = BrewEspressoCommand(barista)
    cappuccino_order = BrewCappuccinoCommand(barista)
    latte_order = BrewLatteCommand(barista)

    # Taking the orders
    coffee_shop.take_order(espresso_order)
    coffee_shop.take_order(cappuccino_order)
    coffee_shop.take_order(latte_order)

    # Serve (execute) the orders
    coffee_shop.serve_orders()