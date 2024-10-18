class Employee:
    def __init__(self, company, full_name, salary):
        self.commpany = company
        self.full_name = full_name
        self.salary = salary

    def print_employee(self):
        print(f"Company: {self.commpany}\nFull Name: {self.full_name}\nSalary: {self.salary}")
    