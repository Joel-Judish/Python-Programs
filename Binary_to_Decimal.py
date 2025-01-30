bitString = input("Enter a String of bits: ")
decimal = 0
exponent = len(bitString)-1
for digit in bitString:
    decimal = decimal + int(digit) * 2 ** exponent
    exponent = exponent - 1
print("The Integer value is", decimal)
