# Overriding --> same name in the parent and child
# Child always override the Parent functions
# Super --> Means call my parent functions

class Animal:
    def sound(self):
        print("Animal sound")


class Dog(Animal):
    # pass  # OP : Animal sound ( if we pass this function )

    def sound(self):
        super().sound()  # If we use super() Key --> ( Animal sound ) - will call
        print("Dog sound")



# animal = Animal()
# animal.sound()  # OP : Animal sound

dog = Dog()
dog.sound()  # OP : Dog sound  (# OP : Animal sound ( if we pass this function ))
