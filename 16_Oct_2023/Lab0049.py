# Leap Year
year = int(input("Enter a year\n"))

# if year % 4 == 0:
#     if year % 100 != 0:
#         if year % 200 == 0:
#             print("This is leap year")
#     else:
#             print("This is not leap year")


if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print("This is a leap year")
else:
    print("This is not a leap year")
