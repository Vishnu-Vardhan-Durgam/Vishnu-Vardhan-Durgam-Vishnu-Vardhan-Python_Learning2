my_dict = {"a": 1, "b": 3, "c": 5}
# val = my_dict.pop("a")
# print(val)
print(my_dict)

# popitem() --> is used to remove and return an arbitrary key-value pair (as a tuple) from a dict
val = my_dict.popitem()
print(val) # OP = ('c', 5) -- > anything can be removed

del my_dict
