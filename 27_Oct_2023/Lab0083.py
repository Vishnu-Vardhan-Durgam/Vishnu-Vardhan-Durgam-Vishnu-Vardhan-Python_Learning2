# set - immutable , values cann't be changed , no duplicates allowed ,

# initial black set
set1 = set()  # empty set
print(set1)
print("----")

set2 = set("vishnu")  # set from string
print(set2)
print("----")

set3 = {1, 2, 3, 4, 5, 5, 4}  # normal set ---> no duplicates allowed
# set3[1] = 30 # TypeError: 'set' object does not support item assignment
print(set3)
print(type(set3))

set4 = {"india", "england", "austria", "USA", "india"}
print(set4) # OP = {'india', 'austria', 'england', 'USA'} --> latest value will pick
