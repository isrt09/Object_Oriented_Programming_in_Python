from Math.triangle import Triangle
from Math.rectangular import Rectangle
from Math.circle import Circle
from Math.rambus import Rambus

t  = Triangle()
t.set_width(10)
t.set_height(20)

r = Rectangle()
r.set_width(10)
r.set_height(20)

c = Circle()
c.set_width(30)
c.set_height(40)
area = round(c.get_area(),2)

ram = Rambus()
ram.set_height(40)
ram.set_width(50)

print("Triangle Area is",t.get_area())
print("Rectangle Area is",r.get_area())
print("Circle Area is",area)
print("Rambus Area is",ram.get_area())