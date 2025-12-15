n = int(input("Enter a number: "))

a=1
b=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(a, end=" ")
        a,b=b,a+b
    print()
