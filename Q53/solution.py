n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

choice = input("Enter A for Ascending or D for Descending: ")

if choice == 'A' or choice == 'a':
    arr.sort()
    print("Array in Ascending order:", arr)
elif choice == 'D' or choice == 'd':
    arr.sort(reverse=True)
    print("Array in Descending order:", arr)
else:
    print("Invalid choice")
