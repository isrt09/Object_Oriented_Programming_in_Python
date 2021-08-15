class Animal:
    def __init__(self, name,color):
        self.name  = name
        self.color = color

    def type(self):
        print('Type Name :',self.name)

    def colorName(self):
        print('Color Name :',self.color)

    def call(self):
        print('I am Animal Comunity')

class Duck(Animal):
    def call(self):
        print('I am Duck Animal')

duck = Duck("PeaCock","White")
duck.call()
duck.type()
duck.colorName()

