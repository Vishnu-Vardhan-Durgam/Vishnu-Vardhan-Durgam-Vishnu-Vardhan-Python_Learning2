class Person():

    def __init__(self, name):
        self.name = name
        print("You created a Object")

    def Person_details(self):
        print("Your details are ", self.name)


amit = Person("Amit") # OP : You created a Object
amit.Person_details() # OP : Your details are  Amit

nikhil = Person("Nikhil") # OP : You created a Object
nikhil.Person_details() # OP : Your details are  Nikhil
