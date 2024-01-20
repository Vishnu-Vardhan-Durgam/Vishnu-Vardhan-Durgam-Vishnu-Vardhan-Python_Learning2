# Break and Continue

# Break in while loop

count = 1
while count <= 10:
    print(count)
    if count >= 5:
        break
    count = count + 1

# Break in for loop

for number in range(1, 10):
    print(number)
    if number == 5:
        break
    number = number + 1
