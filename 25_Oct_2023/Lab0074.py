squares = [1, 4, 9, 16, 25, 33]

print(squares.pop(4)) # OP = 25
print(squares)   # POP will remove the index value  # OP = [1, 4, 9, 16, 33]

print("--------------")

print(squares.remove(16)) # OP = None ---> cause just Remove first occurrence of value.
print(squares) # REMOVE will remove the value not the index # OP = [1, 4, 9, 33]
