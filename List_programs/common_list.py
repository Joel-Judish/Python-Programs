m=int(input("Enter the limit for the first list:"))
l=[]
l1=[]
l2=[]
for i in range(m):
    item=int(input("Enter the element for the first list:"))
    l.insert(i,item)
n=int(input("Enter the limit for the second list:"))
for i in range(n):
    item=int(input("Enter the element for the second list:"))
    l1.insert(i,item)
for i in range(m):
    for j in range(n):
        if l[i]==l1[j]:
            l2.append(l[i])
print("The common elements list is:",l2)
            
