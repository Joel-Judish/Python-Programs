n=int(input("Enter the limit:"))
l=[]
for i in range(n):
    item=int(input("Enter the element:"))
    l.insert(i,item)
max=max(l)
min=min(l)
print("The maximum element is",max)
print("The minimum element is",min)
