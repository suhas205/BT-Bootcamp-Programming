n = int(input("Enter number of items: "))
if n <= 0:
    print("Invalid number of items")
    exit()

grand_total = 0
total_qty = 0

for i in range(n):
    code = input("Enter item code: ").strip()

    qty = int(input("Enter quantity: "))
    if qty <= 0:
        print("Invalid quantity")
        exit()

    price = float(input("Enter price: "))
    if price <= 0:
        print("Invalid price")
        exit()

    total = qty * price
    total_qty += qty

    if code.upper() == "PROMO10":
        total -= total * 0.10

    grand_total += total

if grand_total > 10000:
    grand_total -= grand_total * 0.10

if total_qty > 20:
    grand_total -= grand_total * 0.05

member = input("Are you a member (y/n): ").lower()
if member not in ['y', 'n']:
    print("Invalid membership input")
    exit()

if member == 'y':
    grand_total -= grand_total * 0.02

if grand_total < 5000:
    tax = grand_total * 0.05
elif grand_total <= 20000:
    tax = grand_total * 0.10
else:
    tax = grand_total * 0.15

grand_total += tax

mode = input("Payment mode (cash/card): ").lower()
if mode not in ['cash', 'card']:
    print("Invalid payment mode")
    exit()

if mode == "card":
    grand_total += grand_total * 0.02

if grand_total < 500:
    print("Minimum purchase of ₹500 not met")
    exit()

points = int(grand_total // 100)

print("\n--- FINAL INVOICE ---")
print("Final Amount:", round(grand_total, 2))
print("Loyalty Points:", points)
