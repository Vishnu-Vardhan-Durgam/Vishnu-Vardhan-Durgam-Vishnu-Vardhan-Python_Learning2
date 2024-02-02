A = int(input("Enter A Number \n")) # 10
B = int(input("Enter B Number \n")) # 0

try:
    C = A/B
    print(C)
except Exception as error:
    print("You are dividing the value with Zero") # OP : You are dividing the value with Zero