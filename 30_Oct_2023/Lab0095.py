my_dict = {"a": 1, "b": 3, "c": 5}

for k, v in my_dict.items():
    if k == "b":
        print("b is Present") # OP = b is Present

op = "b" in my_dict
op2 = "d" in my_dict

print(op) # OP = True
print(op2) # OP = False

