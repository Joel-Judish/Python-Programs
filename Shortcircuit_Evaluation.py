def even(n):
    return n % 2 == 0

def positive(n):
    print(f"Checking if {n} is positive")
    return n > 0

def large_number(n):
    return even(n) or positive(n)

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if large_number(number):
        print(f"{number} is a large number")
    else:
        print(f"{number} is not a large number")
