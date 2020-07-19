
# Polymorphyism with Inheritence ....
class Teacher:
    def lesson(self):
        print('Taking class in MBA')

class Student(Teacher):
    def lesson(self):
        print('Reading class exam preparation')
    def study(self):
        print('I am taking enroll the course')

aStudent = Student()
aStudent.lesson()
aStudent.study()

# Polymorphyism with Functions & Methods ....

class Teacher:
    def study(self):
        print('Prepare for the lesson')
class Student:
    def study(self):
        print('Prepare for the exam')

aTeacher = Teacher()
aStudent = Student()

for obj in (aTeacher,aStudent):
    obj.study()


# Polymorphic Functions

len("Hello World")
len([1,2,3,4,5])
len((1,2,3,4,5))