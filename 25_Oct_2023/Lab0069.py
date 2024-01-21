# list = collection of items (duplicates are allowed)
#
my_list = [1, 2, 3, 4, 5]
my_list2 = [1, True, "vishnu", 4.25]

print("initial list is:", my_list)  # OP = initial list is: [1, 2, 3, 4, 5]

# indexing
print("Element at index 0 is", my_list[0])  # OP = Element at index 0 is 1
#
# # changing an element
my_list[1] = 20
print("changing element:", my_list)  # OP = Changing element: [1, 20, 3, 4, 5]

# append
my_list.append(10)
print("List after appending:", my_list)  # OP = List after appending: [1, 20, 3, 4, 5, 4]

# extend
my_list.extend([15, 26])
print("List after extend", my_list)  # OP = List after extend [1, 20, 3, 4, 5, 4, 5, 6]

# insert
my_list.insert(1, 'a')
print("After insert:", my_list)  # OP = After insert: [1, 'a', 20, 3, 4, 5, 4, 5, 6]

# remove
my_list.remove('a')
print("after remove:", my_list)  # OP =after remove: [1, 20, 3, 4, 5, 4, 5, 6]

# copy
my_copy_list = my_list.copy()
print("Copy list is:", my_copy_list)  # OP = Copy list is: [1, 20, 3, 4, 5, 4, 5, 6]

# clear
my_list.clear()
print("initial list:", my_list)  # OP = initial list: []

print("Index of my_list", my_copy_list[0])
print("Index of my_list", my_copy_list[1])
print("Index of my_list", my_copy_list[2])
print("Index of my_list", my_copy_list[3])

# sort
my_copy_list.sort()
print(my_copy_list)

# reverse
my_copy_list.reverse()
print(my_copy_list)

# length
print(len(my_copy_list))
