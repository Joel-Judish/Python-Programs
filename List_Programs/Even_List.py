n=int(input("Enter the limit:"))
l=[]
l1=[]
for i in range(n):
    item=int(input("Enter the element:"))
    l.insert(i,item)
for i in range(n):
    if l[i]%2==0:
        l1.append(l[i])
l1.sort()
print("The list of even numbers in ascending order is:",l1)
        
