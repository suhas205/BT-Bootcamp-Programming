arr=[2,3,78,5,6,7]
s=0
for i in range(len(arr)):
    if arr[i]>s:
        s=arr[i]

print("Largest value is", s)

# this fail for negative values so 

arr=[2,3,78,5,6,7]
s=arr[0]
for i in range(1,len(arr)):
    if arr[i]>s:
        s=arr[i]

print("Largest value is", s)