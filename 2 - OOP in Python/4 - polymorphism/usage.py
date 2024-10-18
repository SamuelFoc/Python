from lib.Employee import Employee
from lib.Engineer import Programmer
from lib.Manager import Manager


employee = Employee("Super Company", "Joe Dohn", 100000)
employee.print()
employee.work()

programmer = Programmer("Duper Company", "Jacob Smith", 120000, "Python")
programmer.print()
programmer.work()

manager = Manager("Nice Company", "Rod Stevenson", 65000, 3)
manager.print()
manager.work()

