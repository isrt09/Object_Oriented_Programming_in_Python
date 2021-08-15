# Encapsulation Workflow in Python with Public Mode:

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


# Encapsulation Workflow in Python with Private Mode:

class Rectangle:
    def __init__(self, weight, height):
        self.__height = height
        self.__weight = weight

    def set_height(self,value):
        self.__height = value

    def get_height(self):
        return self.__height

    def set_weight(self, value):
        self.__weight = value

    def get_weight(self):
        return self.__weight

    def get_area(self):
        return self.__height * self.__weight

    def __private_method(self):
        return "Don't allow for private categories"

    def public_method(self):                
        print(self.__height)
        print(self.__private_method())

r1 = Rectangle(300,400)
r1.public_method()
print("Height of Rectangle is",r1.get_height())
print("Weight of Rectangle is",r1.get_weight())
print("Area of Rectangle is",r1.get_area())
print("Area of Rectangle is {} sqft".format(r1.get_area()))


















