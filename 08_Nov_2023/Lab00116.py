# Hierarchical inheritance

class Vehicle:

    def info(self):
        return ("This is a Vehicle")


class Car(Vehicle):

    def info(self):
        return ("This is a Car")


class Bicyle(Vehicle):

    def info(self):
        return ("This is a Bicycle")


car = Car()
bicycle = Bicyle()
print(car.info())
print(bicycle.info())
