m = int(input("Enter the number of key-value pairs in the dictionary Stock: "))
Stock = {}
for i in range(m):
    keys = input("Enter the item name: ")
    values = int(input("Enter the count of item: "))
    Stock[keys] = values
n = int(input("Enter the number of key-value pairs in the dictionary Price: "))
Price = {}
for i in range(n):
    keys = input("Enter the item name: ")
    values = int(input("Enter the price of item: "))
    Price[keys] = values
print("Items in stock",Stock)
print("Price of items",Price)
count=0
while(True):
  x=input('Enter the key of items to be brought:' )
  if x in Stock.keys():
    count=count+Price[x]
    Stock[x]=Stock[x]-1
  else:
    print('Item not found')
    break
print(Stock)
print(Price)
print('Total Price: ',count)
