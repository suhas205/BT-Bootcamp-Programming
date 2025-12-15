taxable_income = float(input("Enter Taxable Income: "))
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

print("Income Tax:", tax)
print("Cess (4%):", cess)
print("Total Tax Payable:", total_tax)
