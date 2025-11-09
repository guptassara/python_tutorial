# @property = Decorator used to define as a property (it can be accessed like an attribute)
# Benifit: Add additional logic when read, write or delete attributes.
# Gives you getter, setter and a deleter method


class Rectangle:
    def __init__(self, width, height):
        self._width = width  # protected by _
        self._height = height  # protected by _

    # Getter method

    @property
    def width(self):
        return f"{self._width: .2f} cm"

    @property
    def height(self):
        return f"{self._height: .2f} cm"

    # Setter method

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("height must be greater than zero")

    # Deleter method

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")


rectangle = Rectangle(3, 4)

rectangle.width = 5
rectangle.height = 9

print(rectangle.width)
print(rectangle.height)

del rectangle.width
del rectangle.height
