# super() = function used in a child class to call methods from a parent class (superclass)
# Allows you to extend the sunctionality of the inherited methods

import math


class Shape:
    def __init__(self, colour, is_filled):
        self.colour = colour
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.colour} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, colour, is_filled, radius):
        super().__init__(colour, is_filled)
        self.radius = radius

    def describe(self):  # method overriding
        print(f"It is a circle of are {self.radius**2 * math.pi}")
        super().describe()


class Square(Shape):
    def __init__(self, colour, is_filled, side):
        super().__init__(colour, is_filled)
        self.side = side

    def describe(self):  # method overriding
        print(f"It is a square of area {self.side * self.side}")
        super().describe()  # extending functionality of describe


class Triangle(Shape):
    def __init__(self, colour, is_filled, width, height):
        super().__init__(colour, is_filled)
        self.width = width
        self.height = height

    def describe(self):  # method overriding
        print(f"It is a triangle of area {self.width * self.height * 0.5}")
        super().describe()


circle = Circle(colour="red", is_filled=True, radius=5)
square = Square(colour="blue", is_filled=True, side=20)
triangle = Triangle(colour="yellow", is_filled=False, width=3, height=9)

print(f"Circle has colour {circle.colour} and radius {circle.radius}")
circle.describe()
print(f"square has colour {square.colour} and side {square.side}")
square.describe()
print(
    f"triangle has colour {triangle.colour} and radius {triangle.width} and height {triangle.height}"
)
triangle.describe()
