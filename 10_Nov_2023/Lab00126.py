a = 10
b = 0

# Exception
# An exception is an event that occurs during the execution of a program
# that disrupts the normal flow of instructions.

try:
    c = a / b
except ZeroDivisionError as error:
# except Exception as error:
    print(error)  # OP : division by zero

