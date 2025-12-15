promocode="PROMO10"
code=input("Enter item code: ")
qty = int(input("Enter quantity: "))
price = float(input("Enter price: "))

grand_total = qty * price
if code.upper() == promocode.upper():
    grand_total=grand_total-grand_total*0.1

print("Total Payable Amount after discount:", grand_total)