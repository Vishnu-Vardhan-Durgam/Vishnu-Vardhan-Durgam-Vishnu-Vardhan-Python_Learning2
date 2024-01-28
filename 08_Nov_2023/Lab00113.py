# Inheritance

# Parent --> Child
# Father --> son
# GF --> Father --> son
# 1BHK -> 1BHK  -> 1BHK

# Single Inheritance


class Animal:

    def Car(self):
        print("Lambo")

    def Speak(self):
        print("Animal can speak")


class Dog(Animal):
    def Speak(self):
        print("Bow Bow")

    def i_want_to_drive(self):
        Animal().Car()

    def speak_animal(self):
        Animal().Speak()


dog = Dog()
dog.Speak()  # OP : Bow Bow
dog.i_want_to_drive() # OP : Lambo
dog.speak_animal() # Animal can speak
