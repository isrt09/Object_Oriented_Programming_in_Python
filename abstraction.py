
from abc import ABC,abstractmethod

class Father(ABC):
    @abstractmethod
    def do_study(self):
        print('Do your homework....')

class Son(Father):
    def __init__(self,name):
        self.name = name
    def call(self):
        print('Daddy, Let me play the game')

    def do_study(self):
       print('I wanna play with',self.name)

child = Son('Teddy Bear')
child.call()
child.do_study()
