# map and filter in the list

sq = lambda x: x * x
result = sq(5)
print(result)

# map functions (where we will go from one item and apply a functions)
numbers = [1, 2, 3, 4, 5]
sq_numbers = []

sq1 = lambda y: y * y
for i in numbers:
    sq_numbers.append(sq1(i))

print(sq_numbers)  # [1, 4, 9, 16, 25]

# Map functions

numbers2 = [6, 7, 8, 9, 10]
sq_numbers2 = list(map(lambda x: x * x, numbers2))  # available for tuple and set as well
print(sq_numbers2)  # [36, 49, 64, 81, 100]

############################

def triple(a):
    return a ** 3


sq_numbers3 = list(map(triple, numbers))
print(sq_numbers3)
