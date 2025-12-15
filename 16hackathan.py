def validate_name(name):
    return name.isalpha() and len(name) <= 50

def validate_empid(empid):
    return empid.isalnum() and 5 <= len(empid) <= 10

def validate_salary(value):
    return value > 0 and value <= 10000000

def validate_allowance(value):
    return value >= 0 and value <= 10000000

def validate_bonus(bonus):
    return 0 <= bonus <= 100

while True:
    name = input("Enter Employee Name: ")
    if validate_name(name):
        break
    print("Invalid name! Use alphabets only (max 50 characters).")

while True:
    empid = input("Enter Employee ID: ")
    if validate_empid(empid):
        break
    print("Invalid EmpID! Must be alphanumeric (5–10 characters).")

while True:
    basic_salary = float(input("Enter Basic Monthly Salary: "))
    if validate_salary(basic_salary):
        break
    print("Invalid Basic Salary!")

while True:
    allowance = float(input("Enter Special Allowance (Monthly): "))
    if validate_allowance(allowance):
        break
    print("Invalid Allowance!")

while True:
    bonus_percent = float(input("Enter Bonus Percentage: "))
    if validate_bonus(bonus_percent):
        break
    print("Invalid Bonus Percentage!")


gross_monthly = basic_salary + allowance
annual_gross = gross_monthly * 12
bonus = (bonus_percent / 100) * annual_gross
annual_gross += bonus


STANDARD_DEDUCTION = 50000
taxable_income = annual_gross - STANDARD_DEDUCTION


tax = 0

if taxable_income <= 300000:
    tax = 0
elif taxable_income <= 600000:
    tax = (taxable_income - 300000) * 0.05
elif taxable_income <= 900000:
    tax = (300000 * 0.05) + (taxable_income - 600000) * 0.10
elif taxable_income <= 1200000:
    tax = (300000 * 0.05) + (300000 * 0.10) + (taxable_income - 900000) * 0.15
elif taxable_income <= 1500000:
    tax = (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (taxable_income - 1200000) * 0.20
else:
    tax = (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (300000 * 0.20) + (taxable_income - 1500000) * 0.30

if taxable_income <= 700000:
    tax = 0

cess = tax * 0.04
total_tax = tax + cess


net_salary = annual_gross - total_tax


print("\n" + "=" * 40)
print("        EMPLOYEE TAX REPORT")
print("=" * 40)
print(f"Name                  : {name}")
print(f"Employee ID           : {empid}")
print(f"Gross Monthly Salary  : ₹{gross_monthly:,.2f}")
print(f"Annual Gross Salary   : ₹{annual_gross:,.2f}")
print(f"Standard Deduction    : ₹50,000")
print(f"Taxable Income        : ₹{taxable_income:,.2f}")
print(f"Income Tax            : ₹{tax:,.2f}")
print(f"Health & Edu Cess 4%  : ₹{cess:,.2f}")
print(f"Total Tax Payable     : ₹{total_tax:,.2f}")
print(f"Annual Net Salary     : ₹{net_salary:,.2f}")
print("=" * 40)
