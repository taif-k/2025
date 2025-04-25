import sys,os
sys.path.append(os.getcwd())

from python.OOPS.Individual_Programs.encapsulation_intro import University

data = University()
data.one()
data.name 
data._age 
print(data._age)

class Tst:
    def __init__(self,name2,age2):
        self.name2 = name2
        self.age2 = age2

hi = Tst(data.name,data._age)
print(hi.age2)

