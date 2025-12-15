n = int(input("Enter a number: "))

a = 0
while n > 0:
    x = n % 10
    a = a * 10 + x
    n //= 10

print("The number reversed:", a)


#need to use the integer devision
