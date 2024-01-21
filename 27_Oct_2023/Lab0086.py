# scopping of data

num = 20


def multiply_by_10(n):
    n *= 10
    num = n  # changing the value inside the function
    print("value of num inside function:", num)  # OP = value of num inside function: 200
    return n


multiply_by_10(num)
# op = multiply_by_10(num)
# print(op)  # OP = 200
print("value of num outside function:", num)  # OP = value of num outside function: 20
