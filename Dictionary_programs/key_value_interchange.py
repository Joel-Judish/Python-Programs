n = int(input("Enter the number of key-value pairs in the dictionary: "))
dict = {}
for i in range(n):
    keys = input("Enter the key: ")
    values = input("Enter the value: ")
    dict[keys] = values
print("Original Dictionary:",dict)
dict1 = {}
for key, value in dict.items():
    dict1[value] = key
print("New dictionary after interchanging key and value: ",dict1)
