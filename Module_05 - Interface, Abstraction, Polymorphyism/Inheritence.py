class Food:
    def __init__(self,_name, _season,_period):
        self.name = _name
        self.season = _season
        self.period = _period

    def getName(self):
        return self.name

    def getCountry(self,_country):
        return _country

    def getDistrict(self,_district):
        return _district

    def getPrice(self):
        return "150 Taka/kg"

orange = Food("Orange", "Summer", "July~September")
mango  = Food("Mango", "Summer", "July~September")
apple  = Food("Apple", "Summer", "July~September")

print(orange.getName())
print(orange.getCountry("Bhutan"))
print(orange.getDistrict("Thimpu"))
print(orange.getPrice())
print(orange.season)
print(orange.period)
print(type(orange))

print("".center(50,"="))
print(mango.getName())
print(mango.getCountry("Bangladesh"))
print(mango.getDistrict("Rajshahi"))
print(mango.getPrice())
print(mango.season)
print(mango.period)
print(type(mango))

print("".center(50,"="))
print(apple.getName())
print(apple.getCountry("India"))
print(apple.getDistrict("Mumbai"))
print(apple.getPrice())
print(apple.season)
print(apple.period)
print(type(apple))
print("".center(50,"="))

class Student:
    def __init__(self,name,age,grade):
        self.name  = name
        self.age   = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self,name,max_students):
        self.name         = name
        self.max_students = max_students
        self.students     = []

    def add_student(self,student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_score(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

s1 = Student("Mazed","31",340)
s2 = Student("Mizan","32",440)
s3 = Student("Mamun","33",640)

s = [s1, s2, s3]
for student in s:
    print(student.name)

c1 = Course("BBA",50)
c2 = Course("MBA",30)
c3 = Course("P.hD",10)

c = [c1, c2, c3]

c1.add_student(s1)
c2.add_student(s2)
c3.add_student(s3)

print(c1.get_average_score())

class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age  = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I have to say\n")

class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color =  color

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and color {self.color}")

    def speak(self):
        print("Meow\n")

class Dog(Pet):
    def speak(self):
        print("Bark\n")

class Fish(Pet):
    pass

p = Pet("John Smith",35)
p.show()
p.speak()

c = Cat("Maria Paula",25,"asian")
c.show()
c.speak()

print("".center(50,"="))

class Person:
    number_of_people = 5

    def __init__(self,name):
        self.name = name
        Person.number_of_people += 1

p1 = Person("Ricky Ponting")
print(p1.number_of_people)

p2 = Person("John Cena")
print(p2.number_of_people)

p3 = Person("Undertaker")
print(p3.number_of_people)
