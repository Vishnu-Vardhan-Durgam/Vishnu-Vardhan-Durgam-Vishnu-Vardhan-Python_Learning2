# File IO in Python

file = open("Lab00132_File.txt", 'r')
print(file.read())
file.close() # OP : This is Vishnu Secret Message

# Append

file2 = open("Lab00132_File.txt", 'a')
file2.write(" --> Yes Yes")
file2.close()

file = open("Lab00132_File.txt", 'r')
print(file.read())
file.close() # OP :  This is Vishnu Secret Message --> Yes Yes


#  FileNotFoundError

try:
    file = open("Lab00133_File.txt", 'r')
    print(file.read())
    file.close()  # OP :  This is Vishnu Secret Message --> Yes Yes
except FileNotFoundError as e:
    print("File not found", e) # OP : File not found [Errno 2] No such file or directory: 'Lab00133_File.txt'
