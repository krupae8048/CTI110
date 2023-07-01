# CTI-110
# P3HW2 - Salary
# KrupaEdward
# 29June2023
#This program evaluates salary based on hours worked, taking into account overtime rates.
#User inputs Name, how many hours they have worked, and their current pay rate

employee_name = input("Enter employee's name:")
hours_worked = float(input("Enter number of hours worked:"))
pay_rate = float(input("Enter employee's pay rate:"))

print ("-"*30)
print ("Employee name: ", employee_name)
print()
print("Hours Worked Pay Rate Overtime Overtime Pay RegHour Pay Gross Pay")
print("-"*140)

#Program determines if overtime pay is applied if the hours worked exceeds 40 hours
#If hours are below 40, program assigns a 0

if hours_worked > 40:
    overtime = hours_worked-40

else:
    overtime = 0

#If hours worked is greater than 40, program applies time and a half to the extra hours worked

reg_pay = hours_worked * pay_rate
overtime_pay = 1.5 * (overtime * pay_rate)
gross_pay = reg_pay + overtime_pay

print(hours_worked, " ", "$",(f'{pay_rate: .2f}'), " ", (f'{overtime: .1f}'), " ", "$", (f'{overtime_pay: .2f}'), " ", "$",(f'{reg_pay: .2f}')," ", "$",(f'{gross_pay: .2f}'))
