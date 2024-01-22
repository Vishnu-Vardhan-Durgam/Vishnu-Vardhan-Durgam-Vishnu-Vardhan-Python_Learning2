my_dict = {"a": 1, "b": 3, "c": 5, "a": 95}
print(my_dict)  # OP = {'a': 95, 'b': 3, 'c': 5}

# if you have duplicate keys , latest key value will be used

keys = my_dict.keys()
values = my_dict.values()
print(keys)  # OP = dict_keys(['a', 'b', 'c'])
# Get all the keys into list
list_keys = list(keys)
print(list_keys)  # OP = ['a', 'b', 'c']
print(list_keys[0])  # OP = a
print(list_keys[1])  # OP = b
print(list_keys[2])  # OP =  c
print(values)  # OP = dict_values([95, 3, 5])

my_dict = {"a": 1, "b": 3, "c": 5, "a": 95}

# To clear  ######################
# my_dict.clear()
# print(my_dict) # OP = {}

# to copy #######################3
copy_my_dict = my_dict.copy()
print(copy_my_dict)

print("------")

# to convert all the items into set ##
print(my_dict.items()) # OP = dict_items([('a', 95), ('b', 3), ('c', 5)])
set_dict = set(my_dict.items())
print(set_dict) # OP = {('b', 3), ('c', 5), ('a', 95)}