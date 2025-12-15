grand_total=float(input("Enter Grand Total: "))
total_quantity=int(input("Enter Total Quantity: "))

disc=0
disc_add=0
#or directly subtract wiht the grand_total directly

if grand_total>10000:
    disc=grand_total*0.1

if total_quantity>20:
    disc_add=grand_total*0.05

pay_total=grand_total-disc-disc_add
print("Total Payable Amount:", pay_total)
