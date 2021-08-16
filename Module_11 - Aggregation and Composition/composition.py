class Salary:
    def __init__(self,pay,bonus):
        self.pay   = pay
        self.bonus = bonus

    def annual_salary(self):
        return self.pay * 12 + self.bonus

class Employee:
    def __init__(self,name,age,pay,bonus):
        self.name  = name
        self.age   = age
        self.others= Salary(pay,bonus)

    def full_salary(self):
        return self.others.annual_salary()

emp = Employee('TechnoVista Limited','45',10000,5000)
print("The Total Salary = ",emp.full_salary())