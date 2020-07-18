class Student:
    def __init__(self,name, department):
        self.name       = name
        self.department = department
    def getInfo(self):
        print('Stuent Name is :',self.name)
        print('Department Name is :',self.department)

aStudent = Student('Mazedur Rahman','Applied Statistics')
aStudent.getInfo()