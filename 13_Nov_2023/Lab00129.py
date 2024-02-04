# try:
#     result = 10 / 0  # Attempting to divide by Zero
# except ZeroDivisionError as error:
#     print("Error", error)  # ---> Error division by zero

# Example is Division by Zero exception

try:
    x = int(input("Enter a number:"))
    result = 10 / x
    print(result)
except ZeroDivisionError as error:
    print("Error -- 0:", error)  # ---> Error division by zero
except ValueError as error:
    print1("Error -- V:", error)  # ---> Error: invalid literal for int() with base 10: 'vishnu'
except NameError as error:
    print("Error -- N:", error)
except IndentationError as error:
    print("Error -- I:", error)
finally:
    print("I will be executed any how")
