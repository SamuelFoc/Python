from lib.AbstractEmployee import AbstractEmployee

class Manager(AbstractEmployee):
    def __init__(self, company, full_name, salary, team_size):
        super().__init__(company, full_name, salary)
        self._team_size = team_size

    def print(self):
        super().print()
        print(f"Team Size: {self._team_size}")

    @property
    def team_size(self):
        return self._team_size
    
    @team_size.setter
    def team_size(self, new_team_size):
        self._team_size = new_team_size

    #! OVERRIDE THE WORK METHOD
    def work(self):
        print(f"Working as a manager..")

    