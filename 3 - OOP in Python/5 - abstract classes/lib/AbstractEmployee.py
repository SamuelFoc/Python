from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
    def __init__(self, company, full_name, salary):
        self._commpany = company
        self._full_name = full_name
        self._salary = salary

    @abstractmethod
    def work(self):
        """Print how the employee works"""
        pass

    def print(self):
        print("\n---")
        print(f"Company: {self._commpany}\nFull Name: {self._full_name}\nSalary: {self._salary}")

    @property
    def company(self):
        return self._commpany
    
    @company.setter
    def company(self, new_company):
        self._commpany = new_company

    @property
    def name(self):
        return self._full_name
    
    @name.setter
    def name(self, new_name):
        self._full_name = new_name

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = new_salary
