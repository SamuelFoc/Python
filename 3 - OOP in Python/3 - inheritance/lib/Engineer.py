from lib.Employee import Employee

class Programmer(Employee):
    def __init__(self, company, full_name, salary, programming_language):
        super().__init__(company, full_name, salary)
        self._programming_language = programming_language

    def print(self):
        super().print()
        print(f"Programming Lang.: {self._programming_language}")

    @property
    def p_language(self):
        return self._programming_language
    
    @p_language.setter
    def p_language(self, new_programming_language):
        self._programming_language = new_programming_language

    

    