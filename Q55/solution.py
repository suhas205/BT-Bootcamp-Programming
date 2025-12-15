r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

arr = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input("Enter element: ")))
    arr.append(row)

print("\n2D Array elements row-wise:")
for i in range(r):
    for j in range(c):
        print(arr[i][j], end=" ")
    print()
