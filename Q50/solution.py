arr=[1,2,3,4,5,6,7,8,9]

odd=0
even=0

for i in range(len(arr)):
    if arr[i]%2==0:
        even+=1
    else:
        odd+=1


print ("Odd count is :",odd)
print ("Even count is :",even)
