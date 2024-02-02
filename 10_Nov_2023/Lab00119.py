# Polymorphism
# ABC
# Exception

# Polymorphism - OOP's
# object --> behave differently based on the sti
# Person --> Amit , vishnu --> talk() ,Amit can talk in Hindi , Vishnu can talk in english

class Shape:
    def area(self):
        print("Area of Shape")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shape1 = Rectangle(3, 4)
print(shape1.area()) # OP : 12

shape2 = Circle(10)
print(shape2.area()) # OP : 314.0

shape3 = Shape()
shape3.area() # OP : Area of Shape
# print(shape3.area()) # OP : None
