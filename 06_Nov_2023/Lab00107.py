# class  --> is Blueprint to create objects
# objects --> are real world identity
# constructor - way to initialize objects

class Car:
    name = "Pramod"

    def __init__(self, make, model):
        self.make = make
        self.model = model
        print("i will be called first")

    def start_engine(self):
        print("Starting a car", self.make, self.model)


car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civil")

car1.start_engine()
car2.start_engine()
