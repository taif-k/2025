class Shape:
    def __init__(self):
        pass

    def area(self):
        print("Calculating Area of shapes: ")

class square(Shape):
    def area(self,param1):
        print(f"Calculated Area of Square: {param1 * param1}")

class Circle(Shape):
    def area(self,param1,param2=0):
        print(f"Calculated Area of Circle: {3.14 * param1 ** 2}")

obj = Circle()
obj.area(9)
