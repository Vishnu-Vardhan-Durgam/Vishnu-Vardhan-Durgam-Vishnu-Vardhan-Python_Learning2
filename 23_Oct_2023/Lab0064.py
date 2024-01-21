# palindrome
# reverse the string and match with the old string it should be same
# 1 by using  a traditional method
# build in functions


def reverse_string(input_string):
    reverse_str = ""
    for char in input_string:
        reverse_str = char + reverse_str
    return reverse_str


original_str = "NAMAN" # MADAM ,
rev_str = reverse_string(original_str)
print(rev_str)

if original_str == rev_str:
  print("This is palindrome")
else:
  print("This is not")
