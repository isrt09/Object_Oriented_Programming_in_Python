# Inheritence Workflow in Python:
class Polygon:
    __height = None
    __width  = None

    def set_values(self,height,width):
        self.__height = height
        self.__width  = width
    
class Triangle(Polygon):
    def get_area(self):
        return self.__height * self.__width

t1 = Triangle()
t1.set_values(10,20)
print(t1.get_area())


# Inheritence & Encapsulation Workflow in Python:
# Base Class
class Polygon:
    __height = None
    __width  = None

    def set_values(self,height,width):
        self.__height = height
        self.__width  = width

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

# SubClass i.e. Triangle, Rectangle
class Triangle(Polygon):
    def get_area(self):
        return self.get_height() *self.get_width() / 2

class Rectangle(Polygon):
    def get_area(self):
        return  self.get_height() * self.get_width()

t1 = Triangle()
t1.set_values(10,20)
print("Triangle Area is",t1.get_area())

r1 = Rectangle()
r1.set_values(10,20)
print("Rectangular Area is",r1.get_area())

