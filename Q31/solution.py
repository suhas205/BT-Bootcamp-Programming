total = float(input("Enter final amount: "))
mode = input("Payment mode (cash/card): ")

if mode == "card":
    surcharge = total * 0.02
    total += surcharge
    print("Surcharge:", surcharge)

print("Payable Amount:", total)
