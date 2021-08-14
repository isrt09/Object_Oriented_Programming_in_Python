class Person:
    number_of_people = 0

    def __init__(self,name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_peoples(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Ricky Ponting")
p2 = Person("John Cena")
p3 = Person("Undertaker")

print(Person.number_of_peoples())