#!/usr/bin/python3
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)

    def get_picture(self):
        shape = ''
        if self.width or self.height <= 50:
            shape += ('*' * self.width + '\n') * self.height
            return shape
        else:
            return 'Too big for picture'

    def get_amount_inside(self, shape):
        amount = self.get_area() // shape.get_area()
        return amount



class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)

    def set_width(self, width):
        super().set_width(width)
        super().set_height(width)

    def set_width(self, height):
        super().set_width(height)
        super().set_height(height)


a = Rectangle(4,3)
