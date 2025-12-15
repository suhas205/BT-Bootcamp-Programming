nc=int(input("Enter number of rows: "))

n=1
c=0
for i in range(1,nc+1):
    for j in range(i):
        if c%2==0:
            print(n*n,end=" ")
        else:
            print(-(n*n),end=" ")
        n+=1
        c+=1
    print()        