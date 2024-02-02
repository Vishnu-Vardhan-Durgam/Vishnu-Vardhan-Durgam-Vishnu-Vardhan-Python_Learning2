# Abstraction - OOP's
# Hiding the details and showing what is required

# to represent complex systems by simplifying and hiding Unnecessary details

# ABC -- Abstract base class
# Abstract base methods



# Animal(Speak) --> Dog , Cat , Tigor

from abc import ABC, abstractmethod


class Animal(ABC):

    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        return "Bow Bow"


class Cat(Animal):

    def sound(self):
        return "Meow Meow"


class Tigor(Animal):
    # pass
    def sound(self):
        return "Roar -- Grrrr"


dog = Dog()
print(dog.sound())  # OP : Bow Bow

cat = Cat()
print(cat.sound())  # OP : Meow Meow

tigor = Tigor()
print(tigor.sound())  # OP : Roar -- Grrrr
