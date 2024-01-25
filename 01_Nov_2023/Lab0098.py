numbers = [1, -2, 3, 4, -5, 6, -7, 8, 9, -10]


# filter --> Numbers elements can be less or equal
def is_pos(num):
    return num > 0


positive_numbers = filter(is_pos, numbers)
# even_numbers = map(is_even, numbers) # OP : [False, True, False, True, False, True, False, True, False, True]

positive_numbers_list = list(positive_numbers)
print(positive_numbers_list)  # OP : [1, 3, 4, 6, 8, 9]

