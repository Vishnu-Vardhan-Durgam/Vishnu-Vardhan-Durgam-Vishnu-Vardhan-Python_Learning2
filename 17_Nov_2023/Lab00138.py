# with open("read.txt",'r') as file:
#     content = file.read()
#     print(content) # OP : Hello world , This is a text file


# with open("read.txt",'r') as file:
#     content = file.readline()
#     print(content) # OP : Hello world (one line will print)

with open("read.txt", 'r') as file:
    lines = file.readlines()
    print(lines)  # OP : ['Hello world\n', 'This is a text file']
    for line in lines:
        print(line,end="")  # OP : Hello world (end="" -->will remove the spaces)
                            # : This is a text file
