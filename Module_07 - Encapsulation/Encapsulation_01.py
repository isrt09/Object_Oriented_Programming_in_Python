# Encapsulation Workflow in Python:
class Rectangle:

    def __init__(self, weight, height):
        self.height = height
        self.weight = weight

r1 = Rectangle(200,300)
print("Area of Rectangle is",r1.height * r1.weight)
print("Area of Rectangle is {} square feet".format(r1.height * r1.weight))