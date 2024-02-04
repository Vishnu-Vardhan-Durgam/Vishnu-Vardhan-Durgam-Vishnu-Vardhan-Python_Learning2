try:
    # Open the file in read mode
    file = open("Lab00132_File.txt", 'r')
    # Read the contents of the file
    contents = file.read()
    print(contents)
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("An error occurred while reading the file")
else:
    print("File reading completed successfully")
