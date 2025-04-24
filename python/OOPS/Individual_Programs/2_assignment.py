
class Person:
    def __init__(self,name):
        self.name = name
        self.greet()

    def greet(self):
        print(f"{self.name}, Welcome to OOPS classes!")


ask_username = input("Enter name: ")
person1 = Person(ask_username)