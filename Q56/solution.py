r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

arr = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input("Enter element: ")))
    arr.append(row)

print("\n2D Array elements row-wise:")
s=0
for i in range(r):
    for j in range(c):
        s+=arr[i][j]

print("Sum of all elements is:", s )
        
   
