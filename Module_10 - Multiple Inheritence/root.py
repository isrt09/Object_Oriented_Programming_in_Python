from Math.triangle import Triangle
from Math.rectangular import Rectangle
from Math.circle import Circle
from Math.rambus import Rambus

t  = Triangle()
t.set_width(10)
t.set_height(20)
t.set_color("Red")

r = Rectangle()
r.set_width(10)
r.set_height(20)
r.set_color("Green")

c = Circle()
c.set_width(30)
c.set_height(40)
c.set_color("Blue")
area = round(c.get_area(),2)

ram = Rambus()
ram.set_height(40)
ram.set_width(50)
ram.set_color("Yellow")

print("Triangle Area is",t.get_area())
print("Triangle Color is",t.get_color())
print("".center(50,"="))

print("Rectangle Area is",r.get_area())
print("Rectangle Color is",r.get_color())
print("".center(50,"="))

print("Circle Area is",area)
print("Circle Color is",c.get_color())
print("".center(50,"="))

print("Rambus Area is",ram.get_area())
print("Rambus Color is",ram.get_color())
print("".center(50,"="))