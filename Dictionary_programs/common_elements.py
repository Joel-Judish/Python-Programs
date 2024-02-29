m = int(input("Enter the number of key-value pairs in the dictionary d1: "))
d1 = {}
for i in range(m):
    keys = input("Enter the key: ")
    values = input("Enter the value: ")
    d1[keys] = values
n = int(input("Enter the number of key-value pairs in the dictionary d2: "))
d2 = {}
for i in range(n):
    keys = input("Enter the key: ")
    values = input("Enter the value: ")
    d2[keys] = values
common_keys = d1.keys() & d2.keys()
print("Common keys between D1 and D2 are:")
for key in common_keys:
    print(key)
