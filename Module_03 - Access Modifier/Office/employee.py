
class Employee:
    def __init__(self, name, designation, salary, bonus):
        self.name        = name
        self.desgination = designation
        self.salary      = salary
        self.bonus       = bonus
        self.promotion   = ""

    def monthly_gross_salary(self):
        return self.salary / 12

    def salary_bonus(self):
        return self.salary *  (self.bonus / 100)

    def __get_employeeID(self):
        return "1231-222-4567"

    def get_ID(self):
        return self.__get_employeeID()

