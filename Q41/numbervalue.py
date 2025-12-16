n = int(input("Enter number: "))

words = {
    0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
    5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
}

rev = 0
temp = n

while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10

while rev > 0:
    digit = rev % 10
    print(words[digit], end=" ")
    rev //= 10

#other way of doing it like  string way

n = input("Enter number: ")

words = {
    '0': "Zero", '1': "One", '2': "Two", '3': "Three", '4': "Four",
    '5': "Five", '6': "Six", '7': "Seven", '8': "Eight", '9': "Nine"
}

for digit in n:
    print(words[digit], end=" ")
