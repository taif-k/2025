from abc import ABC,abstractmethod
import random

class Department(ABC):
    def __init__(self):
        self.department1 = "HR"
        self.department2 = "Operations"
        self.department3 = "R&D"
        self.teamsize = random.randrange(1,12)

    @abstractmethod
    def team_size(self):
        pass

class HR(Department):
    def __init__(self):
        super().__init__()
        
    def recruitment(self):
        print(f"{self.department1} takes care of recruitment process")

    def team_size(self):
        print(f"Team Size is {self.teamsize}")

class  Operations(Department):
    def __init__(self):
        super().__init__()

    def process_outsource(self):
        print(f"{self.department2} is responsible for business operations")

    def team_size(self):
        print(f"Team size is {self.teamsize}")    

class RnD(Department):
    def __init__(self):
        super().__init__()

    def project_details(self):
        print(f"{self.department3} gathers information for a project")

    def team_size(self):
        print(f"Team size is {self.teamsize}")


object1 = HR()
object1.recruitment()
object1.team_size()
