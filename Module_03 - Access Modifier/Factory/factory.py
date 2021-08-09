from Office.employee import Employee

def main():
    _emp01 = Employee("Sumon Das","Software Engineer",120000,50)
    _emp01.promotion = "Senior Software Engineer"
    print(" Employees Details Information :".center(50,"="))
    print("Annual Gross Salary {:.2f} Taka".format(_emp01.salary))
    print("Monthly Gross Salary {:.2f} Taka".format(_emp01.monthly_gross_salary()))
    print("Salary Bonus {:.2f} Taka (Eid & Festival Bonus)".format(_emp01.salary_bonus()))
    print("Employee ID : {}".format(_emp01.get_ID()))
    print("Approximately Promotion Year 2021 : {}".format(_emp01.promotion))

if __name__ == '__main__':
    main()

