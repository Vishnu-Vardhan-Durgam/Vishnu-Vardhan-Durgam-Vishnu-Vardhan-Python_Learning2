# calculate the area of square and triangle and cube

length = float(input("Enter a number1\n"))
breath = float(input("Enter a number2\n"))
height = float(input("Enter a number3\n"))

area_square = length * breath # number ** 2
area_triangle = (length * breath) / 2 # 1/2(bh)
cube = length * breath * height # number **3

print(area_square)
print(area_triangle)
print(cube)
