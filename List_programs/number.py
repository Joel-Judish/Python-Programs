n=int(input("Enter the limit:"))
num=int(input("Enter the number to be checked:"))
l=[]
l1=[]
for i in range(n):
    item=int(input("Enter the element:"))
    l.insert(i,item)
for i in range(n):
    if l[i]<num:
        l1.append(l[i])
print("The list of elements less than the entered number are:",l1)
