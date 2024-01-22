# orderedDict

my_dict = {"a": 1, "b": 3, "c": 5}
print(my_dict)  # OP = {'a': 1, 'b': 3, 'c': 5}

print(my_dict.pop("a"))  # OP = 1
print(my_dict.pop("b"))  # OP = 3
print(my_dict.pop("c"))  # OP = 5

print(my_dict)  # OP = {}

# OrderedDict
# 1--> Dictionary that remembers insertion order'
# 2 --> An inherited dict maps keys to values.
# key-value pairs based on the order of insertion

from collections import OrderedDict

od = OrderedDict()
od["a"] = 10
od["b"] = 20
od["c"] = 30
od["d"] = 40
od["a"] = 50  # Duplicate ot allowed / latest value accept first
print(od)  # OP = OrderedDict({'a': 50, 'b': 20, 'c': 30, 'd': 40})

# Dict --> it will not keep the Order of insertion
# OrderedDict --> it will keep the order of insertion

keys = list(od.keys())
print(keys) # OP = ['a', 'b', 'c', 'd']
keys_sort = sorted(keys)
print(keys_sort) # OP = ['a', 'b', 'c', 'd']

od2 = OrderedDict()
od2[keys_sort[0]] = 45
od2[keys_sort[2]] = 55
od2[keys_sort[3]] = 65
print(od2) # OP = OrderedDict({'a': 45, 'c': 55, 'd': 65})
