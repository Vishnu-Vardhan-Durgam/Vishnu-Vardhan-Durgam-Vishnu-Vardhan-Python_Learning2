# Logical operators
# and logical AND
# or logical OR
# not logical NOT

# OR GATE - 0 = False , 1 = True #Def --> If atleast one condition is true than the function is True
# A B T/F
# 0 0 F
# 0 1 T
# 1 0 T
# 1 1 T
x = 5
y = 5
print(x >= y)  # OP : True

# AND GATE (works opposite to or gate) - 0 = False , 1 = True #Def --> If atleast one condition is false than the function is False
# A B T/F
# 0 0 F
# 0 1 F
# 1 0 F
# 1 1 T

# NOT - not p = False ,not q = True

p = True
q = False

print(p and q)  # OP : False
print(p or q)  # OP : True
print(not p)  # OP : False
