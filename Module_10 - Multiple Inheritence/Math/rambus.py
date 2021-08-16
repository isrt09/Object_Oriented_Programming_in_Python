from Math.main import Polygon
from Math.shape import Shape

class Rambus(Polygon,Shape):
    def get_area(self):
        return 4 * self.get_width()