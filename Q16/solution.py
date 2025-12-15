name = input("Enter Name: ")
if not name.isalpha() or len(name) > 50:
    print("Invalid Name")
    exit()

empid = input("Enter EmpID: ")
if not empid.isalnum() or len(empid) < 5 or len(empid) > 10:
    print("Invalid EmpID")
    exit()

basic = float(input("Enter Basic Salary: "))
if basic <= 0 or basic > 10000000:
    print("Invalid Basic Salary")
    exit()

allowance = float(input("Enter Allowance: "))
if allowance < 0 or allowance > 10000000:
    print("Invalid Allowance")
    exit()

bonus = float(input("Enter Bonus Percentage: "))
if bonus < 0 or bonus > 100:
    print("Invalid Bonus Percentage")
    exit()

print("All inputs are valid")
