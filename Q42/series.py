n=int(input("Enter number for n value: "))
a=1
b=-5
for i in range(n):
    if i%2==0:
        print(a,end=" ")
        a+=8
    else:
        print(b,end=" ")
        b-=8 
