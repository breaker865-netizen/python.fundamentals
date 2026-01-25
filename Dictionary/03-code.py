phone = dict()
n = int(input("Enter number of entries: "))

# Collecting data
for i in range(n):
    a = input("Enter Name: ")
    b = input("Enter phone no: ")
    phone[a] = b

# Searching data
x = input("Enter the name to be searched: ") # Removed int() conversion

if x in phone:
    print(x, ": phone no =", phone[x])
else:
    print(x, "does not exist.")