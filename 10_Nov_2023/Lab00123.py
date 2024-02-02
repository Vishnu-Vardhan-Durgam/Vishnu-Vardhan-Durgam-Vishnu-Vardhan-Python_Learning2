# Shape --> Rectangle , Circle
# Shape --> Perimeter , Area


from abc import ABC, abstractmethod


class Shape(ABC):

    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        # return 2 * 3.14 * self.radius
        return  3.14 * self.radius * self.radius



rect = Rectangle(4, 5)
print(rect.area())  # Output: 20
print(rect.perimeter())  # Output: 18

circle = Circle(3)
print(circle.area())  # Output: 28.26
print(circle.perimeter())  # Output: 18.84
