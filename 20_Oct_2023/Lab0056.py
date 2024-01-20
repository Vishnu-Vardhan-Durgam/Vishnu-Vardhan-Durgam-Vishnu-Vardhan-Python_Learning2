# Multiple initialisation

# a = 1
# b = 0
# print(a, b) # OP = 1 0

# a ,b, c = (1,2,3)
# print(c) # OP = 3


# fibonaci series
# 0, 0+1 , 0+1+1
# n = could be any number - will calculate its last series/number
# 0,1,2,3,5,8,13


number = int(input("Enter a number\n"))

a, b = 0, 1
while a < number: # or while a < 10(any number):
    print(a, end=' ')
    a, b = b, a + b
