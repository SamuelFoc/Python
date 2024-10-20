class Employee:
    def __init__(self, company, full_name, salary):
        # Initialize the Employee instance with company name, full name, and salary
        # Private fields start with an underscore to indicate they are intended for internal use
        self._company = company  # Fixed typo: 'commpany' to 'company'
        self._full_name = full_name
        self._salary = salary

    def print_employee(self):
        # Print the employee's details: company name, full name, and salary
        print(f"Company: {self._company}\nFull Name: {self._full_name}\nSalary: {self._salary}")

    # Getter for the private field _company, defined using the @property decorator
    # This allows controlled access to the _company attribute
    @property
    def company(self):
        return self._company  # Return the value of the company

    # Setter for the private field _company
    @company.setter
    def company(self, new_company):
        self._company = new_company  # Update the company name

    # Getter for the private field _full_name
    @property
    def name(self):
        return self._full_name  # Return the employee's full name

    # Setter for the private field _full_name
    @name.setter
    def name(self, new_name):
        self._full_name = new_name  # Update the employee's full name

    # Getter for the private field _salary
    @property
    def salary(self):
        return self._salary  # Return the employee's salary

    # Setter for the private field _salary with validation
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salary cannot be negative.")  # Raise an error if salary is negative
        self._salary = new_salary  # Update the salary if valid

    def work(self):
        # Simulate the employee working
        print("I am working..")
