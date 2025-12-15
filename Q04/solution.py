a = 10
b = 20

a, b = b, a

print(a, b)

temp=a
a=b
b=temp
print("After swapping:", a, b)