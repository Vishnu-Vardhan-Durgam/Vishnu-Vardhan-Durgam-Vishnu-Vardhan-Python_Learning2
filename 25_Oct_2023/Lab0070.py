# my_list = [1, 1.5, True, "vishnu"]

# my_list.sort()
# print(my_list) # OP = not supported between instances of 'str' and 'bool'

#########################

squares = [1, 4, 9, 16, 25]
l = squares
l2 = squares.copy()
squares[0] = 33
print(squares)
print(l)
print(l2)
