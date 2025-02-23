def divide_square(n):
    if n%5==0:
        return(n**0.5)
    else:
        return n%5

n=int(input("Enter the Number:"))
print(divide_square(n))
