try:
    x = int(input("Enter a number:"))
    result = 10 / x
    print(result)
except Exception as error:
    print("Error :", error)
finally:  # Optional 
    print("I will be executed any how")