# Single Inheritence
class Mammal(object):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    
class Dog(Mammal):
  def __init__(self):
    print('Dog has four legs.')
    super().__init__('Dog')
    
d1 = Dog()

# Multiple Inheritence
class Animal:
  def __init__(self, Animal):
    print(Animal, 'is an animal.');

class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    super().__init__(mammalName)
    
class NonWingedMammal(Mammal):
  def __init__(self, NonWingedMammal):
    print(NonWingedMammal, "can't fly.")
    super().__init__(NonWingedMammal)

class NonMarineMammal(Mammal):
  def __init__(self, NonMarineMammal):
    print(NonMarineMammal, "can't swim.")
    super().__init__(NonMarineMammal)

class Dog(NonMarineMammal, NonWingedMammal):
  def __init__(self):
    print('Dog has 4 legs.');
    super().__init__('Dog')
    
d = Dog()
print('')
bat = NonMarineMammal('Bat')


# Use of Super
class Animal(object):
  def __init__(self, animal_type):
    print('Animal Type:', animal_type)
    
class Mammal(Animal):
  def __init__(self):

    # call superclass
    super().__init__('Mammal')
    print('Mammals give birth directly')
    
dog = Mammal()

