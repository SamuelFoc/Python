# Import the Employee class from the lib module
from lib.Employee import Employee

# Create an instance of the Employee class with company name, employee name, and salary
employee = Employee("Super Company", "Joe Dohn", 100000)

# Print the details of the employee (company, full name, and salary)
employee.print_employee()

# Use the salary property setter to update the salary
employee.salary = 105000  # This ensures that any validation checks in the setter are applied

# Print the updated details of the employee to see the changes
employee.print_employee()