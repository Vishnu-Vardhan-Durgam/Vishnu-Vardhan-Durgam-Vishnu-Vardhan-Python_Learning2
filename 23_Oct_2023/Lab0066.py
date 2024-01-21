original_string = "VISHNU"


def is_palindrome(original_string):
    rev_str = original_string[::-1]
    print(rev_str)
    if original_string == rev_str:
        print("This is palindrome")
    else:
        print("This is not")

is_palindrome(original_string)
# print(is_palindrome(original_string)) ---> OP : None
