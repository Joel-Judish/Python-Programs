string= input("Enter a string: ")
dict = string.lower().split()
print(dict)
frequencies = {}
for word in dict:
    if word not in frequencies:
        frequencies[word] = 1
    else:
        frequencies[word] += 1
print("Word frequencies: ", frequencies)
