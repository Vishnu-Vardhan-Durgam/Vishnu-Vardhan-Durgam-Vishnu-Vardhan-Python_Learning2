original_string = str(input("Enter any name\n")) # can use any name directly


def rev_string(original_string):
    return ''.join(reversed(original_string)) # '' is a empty char - can enter any char


rev_str = rev_string(original_string)
print(rev_str)
