# factorial
# 5! = 5x4x3x2x1 = 120

number = int(input("Enter a number\n"))

if number < 0:
    print("factorial not possible")
else:
    fact = 1
    for i in range(1, number + 1):
        fact = fact * i # OP = print(i) --> i = 1,2,3,4,5
    print("This fact number is -->", fact)
