numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(numbers)) # OP : <class 'list'>


# even_numbers = [2,4,6,8,10]

# filter --> Numbers elements can be less or equal
def is_even(num):
    return num % 2 == 0


even_numbers = filter(is_even, numbers)
# even_numbers = map(is_even, numbers) # OP : [False, True, False, True, False, True, False, True, False, True]

even_numbers_list = list(even_numbers)
print(even_numbers_list) # OP : [2, 4, 6, 8, 10]
print(type(even_numbers_list)) # OP : <class 'list'>

# op = is_even(2)
# print(op)  # OP : True
