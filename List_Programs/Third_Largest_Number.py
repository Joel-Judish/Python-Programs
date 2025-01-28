n=int(input("Enter the limit:"))
l=[]
for i in range(n):
    item=int(input("Enter the element:"))
    l.insert(i,item)
l.sort(reverse=True)
if len(l)<3:
    print("The list should have atleast 3 numbers")
else:
    print("The 3rd Largest Number is:",l[2])
