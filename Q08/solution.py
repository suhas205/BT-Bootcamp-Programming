a=3
b=8
c=5
if a>b and a>c:
    print("a is largest",a)
elif b>a and b>c:
    print("b is largest",b)
else:   
    print("c is largest",c)

print("we can do it with using max function too")
print("largest is", max(a,b,c))
