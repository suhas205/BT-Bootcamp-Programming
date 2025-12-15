r1 = int(input("Enter row1 size: "))
c1 = int(input("Enter col1 size: "))
r2 = int(input("Enter row2 size: "))
c2 = int(input("Enter col2 size: "))

arr1 = []
arr2 = []
result = []

for i in range(r1):
    row1 = []
    for j in range(c1):
        row1.append(int(input("Enter element for first matrix: ")))
    arr1.append(row1)

for i in range(r2):
    row2 = []
    for j in range(c2):
        row2.append(int(input("Enter element for second matrix: ")))
    arr2.append(row2)

if c1 != r2:
    print("Matrix multiplication not possible")
else:
    for i in range(r1):
        row3 = []
        for j in range(c2):
            s = 0
            for k in range(c1):
                s += arr1[i][k] * arr2[k][j]
            row3.append(s)
        result.append(row3)

    print("Resultant Matrix:")
    for row in result:
        print(row)
