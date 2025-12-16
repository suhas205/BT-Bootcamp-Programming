# Level 7: Admin sets up services of the day
services = ["General Consultation", "Blood Test", "Covid Test", "X-Ray", "CT Scan", "MRI"]
costs = [500, 300, 800, 1500, 4000, 7000]

# Level 1: Patient details (simple validation)
name = input("Enter Patient Name: ")
if name == "":
    print("Invalid name")
    exit()

age = int(input("Enter Age: "))
if age <= 0:
    print("Invalid age")
    exit()

gender = input("Enter Gender: ")
if gender == "":
    print("Invalid gender")
    exit()

contact = input("Enter Contact Number: ")
if contact == "":
    print("Invalid contact number")
    exit()

# Level 2: Display services
print("\nAvailable Services:")
for i in range(len(services)):
    print(f"{i+1}. {services[i]}")

# Remove duplicate selections using set
choices = list(set(map(int, input("\nEnter service numbers separated by space: ").split())))

selected_services = []
selected_costs = []

# Level 3: Fetch selected services and costs
for choice in choices:
    if choice < 1 or choice > len(services):
        print("Invalid service selection")
        exit()
    selected_services.append(services[choice - 1])
    selected_costs.append(costs[choice - 1])

# Level 4: Calculate subtotal
subtotal = sum(selected_costs)

# Level 8: Discounts
if age >= 60:
    subtotal -= subtotal * 0.10

if subtotal > 5000:
    subtotal -= subtotal * 0.05

# Level 5: Apply GST
gst = subtotal * 0.18
grand_total = subtotal + gst

# Level 6: Invoice generation
print("\n-----------------------------------------------")
print("HealWell Care Hospital")
print("Patient Invoice")
print("-----------------------------------------------")

print("\nPatient Information:")
print("Name:", name)
print("Age:", age)
print("Gender:", gender)
print("Contact:", contact)

print("\nServices Availed:")
for i in range(len(selected_services)):
    print(f"{i+1}. {selected_services[i]}: ₹{selected_costs[i]}")

print("\nSubtotal: ₹", round(subtotal, 2))
print("GST (18%): ₹", round(gst, 2))
print("Grand Total: ₹", round(grand_total, 2))

print("\nThank you for choosing HealWell Care Hospital!")
print("-----------------------------------------------")
