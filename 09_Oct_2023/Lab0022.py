# string
# Bunch of char
name = "vishnu vardhan"

#  string functions
#  python immutable in nature  they can't be changed once created

#  capitalize
# Returns a copy of the string with its first letter capitalized
result = name.capitalize()
print(result)  # OP : Vishnu vardhan
print(name)

# ID - Identity ,Address reference
print(id(name))
print(id(result))

# upper case
result2 = name.upper()
print(result2)  # OP : VISHNU VARDHAN

# lower case
result3 = name.lower()
print(result3)  # OP : vishnu vardhan

#  swapcase
#  returns a copy of string with uppercase to lower case and  vise versa

name1 = "vIsHnU"
result4 = name1.swapcase()
print(result4)  # OP : ViShNu

result5 = result4.swapcase()
print(result5)  # OP : vIsHnU

#  Title
#  returns title cased version of the string
#  where words start with an uppercase characters and the remaining characters are lowercase
name5 = "hello world"
print(name5.title())  # OP : Hello World

# replace
text = "hello world"
result_rep = text.replace("world", "Python")
print(result_rep)

# find()
#  returns the lowest index of a substring in the string
#  returns -1 if the substring is not found
text = "hello world"
index = text.find("world")
print(index)  # OP : 6 (index starting from 6)

# count -
count = text.count("l")
print(count) # OP : 3 (3 l's present in hello world)

#  delete
name5 = ["Vishn Vardhan","Durgam"]
print(name5) # OP : ['Vishn Vardhan', 'Durgam']
del name5[1]
print(name5) # # OP : ['Vishn Vardhan']