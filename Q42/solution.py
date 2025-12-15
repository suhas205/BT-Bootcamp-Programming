n = int(input("Enter number of rows: "))

fact = 1
num = 1

print("1")
for i in range(2, n+1):
    for j in range(i):
        fact *= num
        print(fact, end=" ")
        num += 1
    print()
