class Salary:
    def __init__(self,pay,bonus):
        self.pay   = pay
        self.bonus = bonus

    def annual_salary(self):
        return self.pay * 12 + self.bonus

class Employee:
    def __init__(self,name,age,salary):
        self.name  = name
        self.age   = age
        self.others= salary

    def full_salary(self):
        return self.others.annual_salary()

salary   = Salary(10000,5000)
employee = Employee("TechnoVista Ltd",20, salary)
print("The Total Salary = ", employee.full_salary())