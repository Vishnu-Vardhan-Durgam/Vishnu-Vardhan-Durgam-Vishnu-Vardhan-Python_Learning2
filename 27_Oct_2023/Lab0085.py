set1 = {1, 2, 3}
set2 = {4, 5, 6}
my_set1 = set1.union(set2)
print(my_set1)  # OP = {1, 2, 3, 4, 5, 6}

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6}
my_set2 = set1.intersection(set2)
print(my_set2)  # OP = {4, 5}

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6}
my_set3 = set1.difference(set2)
print(my_set3)  # OP = {1, 2, 3}

set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 4, 5, 6}
my_set3 = set1.issubset(set2) # checking of --> set1 is part of set2
print(my_set3) # OP =  False

set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 4,}
my_set4 = set2.issubset(set1) # checking of --> set2 is part of set1
print(my_set4) # OP = True