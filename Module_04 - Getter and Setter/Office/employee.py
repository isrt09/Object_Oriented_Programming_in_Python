
class Employee:
    def __init__(self, name, designation, salary, bonus):
        self.name        = name
        self.desgination = designation
        self.salary      = salary
        self.bonus       = bonus
        self.promotion   = ""
        self.district    = ""
        self.mobile      = ""

    def monthly_gross_salary(self):
        return self.salary / 12

    def salary_bonus(self):
        return self.salary *  (self.bonus / 100)

    def __get_employeeID(self):
        return "1231-222-4567"

    def get_ID(self):
        return self.__get_employeeID()

    # Getter Method
    @property
    def permanent_address(self):
        return self.district

    # Getter Method
    @property
    def getContact(self):
        return self.mobile

    # Setter Method
    @getContact.setter
    def getContact(self, _mobile):
        self.mobile = _mobile

    # Setter Method
    @permanent_address.setter
    def permanent_address(self, address):
        self.district = address
