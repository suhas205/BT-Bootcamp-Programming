total_amount = float(input("Enter total amount: "))
discount_rate = float(input("Enter discount percentage: "))

discount = (total_amount * discount_rate) / 100
final_amount = total_amount - discount

print("Discount Amount =", discount)
print("Amount to Pay =", final_amount)
