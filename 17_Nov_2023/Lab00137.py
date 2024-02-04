# File handling

# How to read a Text and write into it

# Open a file
#  file_object = open("Vishnu.txt", mode)

# modes
# 'r' for reading (default)
# 'w' for writing (creates a new file or truncates an existing one)
# 'a' for appending
# 'b' for binary mode
# '+' for updating (reading and writing)

# Read a file
# Reading entire Content : content = file_object.read()
# line = file_object.readline() for a single line
# lines = file_object.readlines() for all items in list

# Write a file
# writing a string : file_object.write(string)
# writing multiple lines : file_object.writelines(list_of_strings)

# Closing a file
# syntax : file_object.close()

# Read --> Example1
with open("Vishnu.txt", 'r') as anything:
    content = anything.read()
    print(content)  # OP : This is a secret message

# Read --> Example2
with open("TestData.txt", 'r') as anything:
    content = anything.read()
    print(content)  # OP : Admin

# File not found
try:
    with open("TestData2.txt", 'r') as file:
        content = file.read()
        print(content)  # File not found
except FileNotFoundError as error:
    print(error)  # [Errno 2] No such file or directory: 'TestData2.txt'

# write
with open("Example.txt", 'w') as file: # w --> always create a new file
    file.write("Hello World")  # OP : New file created as "Example.txt" with "Hello World" text

# append
with open("Example.txt", 'a') as file:
    file.write("Hello World")  # OP :  "Hello World" text will be added into "Example.txt" file






