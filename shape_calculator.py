class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, new_width):
        if new_width > 0:
            self.width = new_width

    def set_height(self, new_height):
        if new_height > 0:
            self.height = new_height

    def get_area(self):
        if (self.width and self.height) > 0:
            return self.width * self.height
        else:
            return "0"

    def get_perimeter(self):
        if (self.width > 0) and (self.height > 0):
            return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        if (self.width > 0) and (self.height > 0):
            return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        line = ''
        if (self.width > 50) or (self.height > 50):
            return "Too big for picture."
        else:
            pic = '*' * self.width
            for n in range(0, self.height):
                line = pic + "\n" + line
            return line

    #def get_amount_inside(self):

class Square:



import shape_calculator

rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect.get_diagonal())
print(rect)
print(rect.get_picture())
rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
