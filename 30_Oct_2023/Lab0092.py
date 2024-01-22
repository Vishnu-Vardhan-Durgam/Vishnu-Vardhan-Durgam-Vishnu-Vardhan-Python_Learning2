my_dict = {"a": 1, "b": 3, "c": 5}

val = my_dict.pop("a")
print(val)  # OP = 1
print(my_dict)  # OP = {'b': 3}

print(dir(dict))
print("-------")

# Howe to iterate over the dict ?

knights = {"gallahad": "the pure", "robbin": "the power"}
print(len(knights))

for k, v in knights.items():
    print(k, v)  # OP = gallahad the pure & robbin the power
    print(k)  # OP = gallahad & robbin
    # print(v)
