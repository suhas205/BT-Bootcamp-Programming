n = int(input("Enter number of terms: "))

a = 1
for i in range(1, n):
    print(a, end=" ")
    a = a + i * i
print(a)
