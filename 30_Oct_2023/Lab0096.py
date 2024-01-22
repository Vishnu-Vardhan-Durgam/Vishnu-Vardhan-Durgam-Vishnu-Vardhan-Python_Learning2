my_dict = {}
key = input("Enter a key\n")
value = input("Enter a value\n")

my_dict[key] = value
print("Updated dict:", my_dict)  # OP = Updated dict: {'vishnu': '174e987'}

my_dict["age"] = 25
print(my_dict)  # OP = {'name': 'vishnu', 'age': 25}

for key, value in my_dict.items():
    print(key, value)
