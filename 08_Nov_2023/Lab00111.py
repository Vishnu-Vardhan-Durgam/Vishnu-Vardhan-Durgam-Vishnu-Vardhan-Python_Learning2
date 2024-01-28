# Encapsulation

# public var - don't mention anything
# protected  ----   "_" single underscore
# private  ----   "__" double underscore


# variable and function

class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getter and Setter to change the name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name == "John":
            print("Don't set the name") # If --> person.set_name("John")
        else:
            self.__name = name

    def print_details(self):
        print("Your details are", self.__name, self.__age)


person = Person("Amit", 35)
person.print_details() # OP : Your details are Amit 35

# How to change it - Get and Set ?
# Fetch - Get
# Set the value - Constructor

person.set_name("Vishnu")

name = person.get_name()
print(name) # OP : Vishnu

person.print_details() # OP : Your details are Vishnu 35
