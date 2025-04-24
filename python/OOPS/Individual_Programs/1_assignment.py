
class Student:
    def  __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.display_info()

    def display_info(self):
        studentdict = {}
        studentdict["name"] = self.name
        studentdict["age"] = self.age
        studentdict["grade"] = self.grade
        print(studentdict)

student1 = Student("abeer",25,"B")
student2 = Student("akash",25,"A")
