class University:
    university ='IBA, DU'
    def __init__(self,name, course):
        self.name   = name
        self.course = course
    def campus(self):
        print('Our Campus Name is :',self.name)
        print('Our Course is :',self.course)
    @classmethod
    def branch(cls):
        print(cls.university)
obj = University('Dhaka University','MBA')
obj.campus()
obj.branch()



