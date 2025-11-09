# Polymorphism = Greek word that means to "have many forms or faces"
# Poly = Many
# Morphe = Form
#
# TWO WAYS TO ACHIEVE POLYMORPHISM
# 1. Inheritance = An object could be treated of the same type as a parent class
# 2. "Duck typing" = Object must have necessary attributes/methods


import math
from abc import ABC, abstractmethod


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        self.radius = radius

        # def area(self):
        #     return math.pi * self.radius**2
        #
        super().__init__(radius)
        self.topping = topping


shapes = [Circle(2.8), Square(5), Triangle(2, 3), Pizza("Mushroom", 10)]

for shape in shapes:
    print(shape.area())


# circle = Circle(colour="red", is_filled=True, radius=5)
# square = Square(colour="blue", is_filled=True, side=20)
# triangle = Triangle(colour="yellow", is_filled=False, width=3, height=9)

# print(f"Circle has colour {circle.colour} and radius {circle.radius}")
# circle.describe()
# print(f"square has colour {square.colour} and side {square.side}")
# square.describe()
# print(
#     f"triangle has colour {triangle.colour} and radius {triangle.width} and height {triangle.height}"
# )
# triangle.describe()
