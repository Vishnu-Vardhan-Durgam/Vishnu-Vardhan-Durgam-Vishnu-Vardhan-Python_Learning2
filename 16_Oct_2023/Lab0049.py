# Leap Year
year = int(input("Enter a year\n"))

if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print("This is a leap year")
else:
    print("This is not a leap year")

############


year1 = 2024
is_leap_year = False

if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    is_leap_year = True
else:
    is_leap_year = False

print(f'{year1} is {is_leap_year}')
