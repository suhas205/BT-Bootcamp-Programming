arr = [2, 3, 78, 5, 6, 7]
key = int(input("Enter the key to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == key:
        print("Key found at index", i, "The value is", arr[i])
        found = True
        break

if not found:
    print("Key not found")
