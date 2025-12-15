arr=[24,3,78,5,6,7]
s=arr[0]
for i in range(len(arr)):
    if arr[i]<s:
        s=arr[i]

print("minimum value is", s)

