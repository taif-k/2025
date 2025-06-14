class Food:
    def __init__(self):
        pass

    def veg(self):
        print("Food is veg")

    def nonveg(self):
        print(f"Food is non-veg")


class Cuisine(Food):
    def __init__(self):
        pass

    def veg(self,param1,param2=0):
        print(f"food is {param1}")

    def nonveg(self,param1):
        print(f"food is {param1}")    

ask_food = input("Enter food name: ")
obj = Cuisine()
obj.veg(ask_food)

