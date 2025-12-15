n = int(input("Enter number of terms: "))

a = 1
for i in range(1, n):
    print(a, end=" ")
    if i % 4 == 0:
        a += 8
    else:
        a += 4
print(a)
