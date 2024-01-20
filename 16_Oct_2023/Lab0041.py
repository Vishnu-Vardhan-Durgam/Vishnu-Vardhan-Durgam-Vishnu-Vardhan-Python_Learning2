# find the maximum of three numbers using the ternary operator

num1 = float(input("enter the first number\n"))
num2 = float(input("enter the second number\n"))
num3 = float(input("enter the third number\n"))

max_number = num1 if (num1 > num2 and num1 > num3) else (num2 if num2 > num3 else num3)
print(f"The maximum of {num1} ,{num2} and {num3} is: {max_number}")
