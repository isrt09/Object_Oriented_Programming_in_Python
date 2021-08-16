from Math.main import Polygon
from Math.shape import Shape

class Triangle(Polygon,Shape):
    def get_area(self):
        return self.get_width() * self.get_height() / 2