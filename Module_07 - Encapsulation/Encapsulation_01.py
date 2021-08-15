# Encapsulation Workflow in Python:
class Rectangle:
    def __init__(self, weight, height):
        self.height = height
        self.weight = weight

    def set_height(self,value):
        self.height = value

    def get_height(self):
        return self.height

    def set_weight(self, value):
        self.weight = value

    def get_weight(self):
        return self.weight

    def get_area(self):
        return self.height * self.weight

r1 = Rectangle(200,300)
print("Area of Rectangle is",r1.height * r1.weight)
print("Area of Rectangle is {} square feet".format(r1.height * r1.weight))

print("".center(50,"="))

r2 = Rectangle(500,600)
print("Area of Rectangle is",r2.get_area())
print("Area of Rectangle is {} square feet".format(r2.height * r2.weight))

print("".center(50,"="))

r2.set_weight(400)
print("Weight of Rectangle is",r2.get_weight())
print("Height of Rectangle is",r2.get_height())
print("Area of Rectangle is",r2.get_area())
print("Area of Rectangle is {} square feet".format(r2.height * r2.weight))
