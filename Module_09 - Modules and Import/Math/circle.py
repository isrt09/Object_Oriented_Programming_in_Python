from Math.main import Polygon
import math

class Circle(Polygon):
    def get_area(self):
        return (4/3) * math.pi * (self.get_width() ** 2)