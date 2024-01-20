# compare two numbers
num1 = float(input("enter the first number\n"))
num2 = float(input("enter the second number\n"))

result = "greater than" if num1 > num2 else "less than" if num1 < num2 else "equal to"
print(f"{num1} is {result} {num2}")
