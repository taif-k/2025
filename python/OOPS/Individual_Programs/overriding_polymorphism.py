class Shape:
    def __init__(self):
        pass

    def area(self):
        print("Calculating Area of shapes: ")

class square(Shape):
    def area(self,param1,param2):
        print(f"Calculated Area of Square: {param1 * param1}")

class rectangle(Shape):
    def area(self,param1,param2):
        print(f"Calculated Area of Rectangle: {param1 * param2}")

obj = square()
obj.area(9,9)
