from lib.AbstractEmployee import AbstractEmployee
from lib.Engineer import Programmer
from lib.Manager import Manager

#! You're not gonna be able to run this, because you cannot instanciate an
#! abstract class. Comment out the three lines below and it will work perfectly
# employee = AbstractEmployee("Super Company", "Joe Dohn", 100000)
# employee.print()
# employee.work()

programmer = Programmer("Duper Company", "Jacob Smith", 120000, "Python")
programmer.print()
programmer.work()

manager = Manager("Nice Company", "Rod Stevenson", 65000, 3)
manager.print()
manager.work()

