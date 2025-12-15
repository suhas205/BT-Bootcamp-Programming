grand_total=float(input("Enter Grand Total: "))

tax=0

if grand_total<5000:
    tax=grand_total*0.05
elif grand_total<5000 and grand_total<20000:
    tax=grand_total*0.1
elif grand_total>=20000:
    tax=grand_total*0.15

print("Total Tax Payable:", tax)
print("Total Payable Amount:", grand_total+tax)
    