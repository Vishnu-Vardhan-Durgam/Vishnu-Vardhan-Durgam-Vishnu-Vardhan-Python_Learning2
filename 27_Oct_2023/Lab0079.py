# list is mutable (its content can be changed)

my_list = [1, 2, 3, 4, 5, 5]  # duplicates allowed
print(my_list)
my_list[1] = 20
print(my_list)

# tuple is immutable (its content cann't be changed)

# my_list2 = (1, 2, 3, 4, 5, 5)  # duplicates allowed
# print(type(my_list2))
# my_list2[1] = 20  # TypeError: 'tuple' object does not support item assignment
# print(my_list2)

# list can be converted into to tuple

list1 = [1, 2, 3, 4, 5, 5]
print(type(tuple(list1)))  # OP = tuple
