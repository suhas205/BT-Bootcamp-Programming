r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

arr = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input("Enter element: ")))
    arr.append(row)

k=int(input("Enter the target key: "))
f=0
for i in range(r):
    for j in range(c):
        if k==arr[i][j]:
            print("Element found at position:", (i,j))
            f=1
            break
    if f==1: #it will break the outer loop as well
        break    
        
if f==0:
    print("Element not found")
   
