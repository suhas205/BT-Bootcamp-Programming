name = input("Enter student name: ")
m1 = float(input("Enter marks in Subject 1: "))
m2 = float(input("Enter marks in Subject 2: "))
m3 = float(input("Enter marks in Subject 3: "))

total = m1 + m2 + m3
average = total / 3

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)

if average >= 60:
    print("Class Secured: 1st Class")
elif average >= 50:
    print("Class Secured: 2nd Class")
elif average >= 35:
    print("Class Secured: Pass Class")
else:
    print("Class Secured: Fail")
