n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

print("Array elements are:", arr)

arr.reverse()
print("Reversed array elements are:", arr)

x=0
y=n-1
while x<y:
    arr[x],arr[y]=arr[y],arr[x]
    x+=1
    y-=1