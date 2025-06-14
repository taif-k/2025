# .__variable_name ->> private variable  (accessed within a class)
#  ._variable_name ->> protected variable (avoid, unless specified)
#  .variable_name ->> public variable (accessed everywhere)

class University:
    def __init__(self):
        pass

    def one(self):
        self.name = "ipu"
        self._age = 20
        self.__pin = 123

class College_A(University):
    def __init__(self):
        pass
        
obj2 = College_A()
obj2.one()
# print(obj2.name) 