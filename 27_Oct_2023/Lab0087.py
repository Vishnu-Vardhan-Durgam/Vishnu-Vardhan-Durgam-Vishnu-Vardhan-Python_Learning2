list1 = [10, 20, 30, 40]


def multiply_by_10(my_list):
    my_list[0] *= 10
    my_list[1] *= 10
    my_list[2] *= 10
    my_list[3] *= 10


print(list1)
multiply_by_10(list1)
print(list1)
print("-------")

tuple1 = (10, 20, 30, 40)


def multiply_by_10(my_tuple):
    my_tuple[0] *= 10 # TypeError: 'tuple' object does not support item assignment
    my_tuple[1] *= 10
    my_tuple[2] *= 10
    my_tuple[3] *= 10


print(tuple1)
multiply_by_10(tuple1) # OP = TypeError: 'tuple' object does not support item assignment
print(tuple1)
print("-------")
