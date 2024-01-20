# triangle classifier
# eq , iso , scalane

side1 = int(input("Enter num1\n"))
side2 = int(input("Enter num2\n"))
side3 = int(input("Enter num3\n"))

if side1 == side2 == side3:
    print("Equivalent")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("isolated")
else:
    print("scalene")
