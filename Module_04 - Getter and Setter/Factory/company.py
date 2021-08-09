from Factory.person import Person

def main():
    _person = Person("Kara", "Smith")
    _person.bonus_percentage   = 0.51
    _person.base_annual_salary = 55000.00

    monthly_gross_pay     = _person.get_monthly_gross()
    standard_annual_bonus = _person.get_standard_annual_bonus_amount()

    print("Annual Salary : {:.2f}".format(_person.base_annual_salary))
    print("Monthly Gross Salary : {:.2f}".format(monthly_gross_pay))
    print("Annual Standard Bonus : {:.2f}".format(standard_annual_bonus))


if __name__ == '__main__':
    main()