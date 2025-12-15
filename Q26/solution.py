n = int(input("Enter number of items: "))
grand_total = 0

for i in range(n):
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    total = qty * price
    grand_total += total

print("Grand Total:", grand_total)
