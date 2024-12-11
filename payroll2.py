class Payroll:
    def __init__(self, hourly_rate, hours_worked, tax_rate=0, bonus_percentage=0):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.tax_rate = tax_rate
        self.bonus_percentage = bonus_percentage

    def c_basic_salary(self):
        return self.hourly_rate * self.hours_worked

    def c_overtime_pay(self):
        regular_hours = 40
        overtime_rate = 1.5 * self.hourly_rate
        if self.hours_worked > regular_hours:
            overtime_hours = self.hours_worked - regular_hours
            overtime_pay = overtime_hours * overtime_rate
            return overtime_pay
        else:
            return 0 

    def c_tax(self, basic_salary):
        return basic_salary * (self.tax_rate / 100)

    def c_bonus(self, basic_salary):
        return basic_salary * (self.bonus_percentage / 100)

    def c_total_pay(self):
        basic_salary = self.c_basic_salary()
        overtime = self.c_overtime_pay()
        tax_deduction = self.c_tax(basic_salary)
        bonus = self.c_bonus(basic_salary)
        total_pay = basic_salary + overtime - tax_deduction + bonus
        return basic_salary, overtime, tax_deduction, bonus, total_pay

    def c_monthly_salary(self):
        weekly_salary = self.c_basic_salary()
        return weekly_salary * 4


hourly_rate = int(input("Enter the hourly rate: $"))
hours_worked = int(input("Enter the number of hours worked in a week: "))
tax_rate = int(input("Enter the tax rate (in percentage): "))
bonus_percentage = int(input("Enter the bonus percentage: "))

payroll = Payroll(hourly_rate, hours_worked, tax_rate, bonus_percentage)

basic_salary, overtime_pay, tax_deduction, bonus, total_pay = payroll.c_total_pay()

print(f"Basic Salary: ${basic_salary}")
print(f"Overtime Pay: ${overtime_pay}")
print(f"Tax Deduction: ${tax_deduction}")
print(f"Bonus: ${bonus}")
print(f"Total Pay: ${total_pay}")

monthly_salary = payroll.c_monthly_salary()
print(f"Monthly Salary (4 weeks): ${monthly_salary}")
