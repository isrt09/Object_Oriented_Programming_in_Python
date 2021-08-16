from Math.main import Polygon
from Math.shape import Shape
import math

class Circle(Polygon,Shape):
    def get_area(self):
        return (4/3) * math.pi * (self.get_width() ** 2)