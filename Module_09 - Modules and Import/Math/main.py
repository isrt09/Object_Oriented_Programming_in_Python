class Polygon:
    __height = None
    __width  = None

    def set_height(self,value):
        self.__height = value

    def get_height(self):
        return self.__height

    def set_width(self, value):
        self.__width = value

    def get_width(self):
        return self.__width

    def get_area(self):
        return self.get_width() * self.get_height()


