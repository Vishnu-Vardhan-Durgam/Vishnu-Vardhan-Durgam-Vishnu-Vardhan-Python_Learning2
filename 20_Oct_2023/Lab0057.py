# match
# similar to switch in JAVA

number = int(input("Enter a number\n"))

match number:
    case 1:
        print("You have entered 1")
    case 2:
        print("You have entered 2")
    case _ :
        print("No idea")
