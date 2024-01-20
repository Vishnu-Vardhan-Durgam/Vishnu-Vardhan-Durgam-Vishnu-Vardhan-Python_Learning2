# functions

# output = max(1, 3)  # built in function
# print(output)

# functions are block of code
# 1. built in functions are created by python guys
# so that you can use them without creating your own

# 2. custom functions - you can create a function which is a block of code, anyone can use it

# a = int(input("enter a number a\n"))
# b = int(input("enter a number b\n"))
# print(a + b)


def sum(a, b):
    return a + b

a = int(input("enter a number a\n"))
b = int(input("enter a number b\n"))
print(sum(a, b))

print(sum(20,30))
