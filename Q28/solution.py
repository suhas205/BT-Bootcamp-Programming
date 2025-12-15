grand_total=float(input("Enter Grand Total: "))

choice=input("Apply discount? (y/n): ")

if choice=='y' or choice=='Y':
    print("Total Payable Amount after discount:", grand_total-grand_total*0.02)
else:
    print("Total Payable Amount:", grand_total)

#keep the code simple as possiable 


