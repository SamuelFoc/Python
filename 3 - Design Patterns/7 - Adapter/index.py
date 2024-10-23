# Modern Coffee Machine with a brew_coffee() method
class CoffeeMachine:
    def brew_coffee(self):
        print("Brewing coffee with the modern Coffee Machine")

# Old Coffee Brewer with a different interface (start method)
class OldCoffeeBrewer:
    def start(self):
        print("Brewing coffee with the old Coffee Brewer")

# Adapter to make OldCoffeeBrewer compatible with CoffeeMachine interface
class CoffeeMachineAdapter:
    def __init__(self, old_coffee_brewer: OldCoffeeBrewer):
        self.old_coffee_brewer = old_coffee_brewer

    # Adapt the brew_coffee() method to call the start() method of OldCoffeeBrewer
    def brew_coffee(self):
        self.old_coffee_brewer.start()

# Example usage
if __name__ == "__main__":
    # Modern Coffee Machine
    modern_machine = CoffeeMachine()
    modern_machine.brew_coffee()

    # Old Coffee Brewer
    old_brewer = OldCoffeeBrewer()

    # Use the adapter to make the old brewer compatible with the new system
    adapter = CoffeeMachineAdapter(old_brewer)
    adapter.brew_coffee()  # This will internally call old_brewer.start()
