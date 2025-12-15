n = int(input("Enter number of elements: "))
k=int(input("Enter the target key: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

arr.sort()
f=0
i=0
j=n-1
while i<=j:
    m=(i+j)//2
    if arr[m]==k:
        print("The index is :",m)
        f=1
        break 
    elif arr[m]>k:
        j=m-1
    else:
        i=m+1    

if f==0:
    print("Element not found")


