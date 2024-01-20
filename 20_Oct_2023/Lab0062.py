# sum of the number

num = int(input("Enter a number\n"))
# num = 12345
sum = 0

while num != 0:
    digit = int(num % 10)
    sum += digit  # 0+digit
    num = num / 10

print(sum)


#############

def getSum(n):
    sum = 0
    while (n != 0):
        sum = sum + (n % 10)
        n = n // 10
    return sum


n = 569
print(getSum(n))
