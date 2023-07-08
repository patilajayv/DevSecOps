print("|111ICalculator|11111")
print("Select Action: 1) addition 2) multiplication 3) subtraction 4) division")

A = input("(1/2/3/4)? ")

if (A == '1'):
    print("You have selected addition")
    b = int(input("Num1: "))
    c = int(input("Num2: "))
    result = b + c
    print("Result:", result)
elif( A == '2'):
    print("You have selected multiplication")
    b = int(input("Num1: "))
    c = int(input("Num2: "))
    result = b * c
    print("Result:", result)
elif (A == '3'):
    print("You have selected subtraction")
    b = int(input("Num1: "))
    c = int(input("Num2: "))
    result = b - c
    print("Result:", result)
elif (A == '4'):
    print("You have selected division")
    b = int(input("Num1: "))
    c = int(input("Num2: "))
    result = b / c
    print("Result:", result)
else:
    print("Invalid input")