class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

 	# Set width and height to atribute
    def set_width(self, new_width):
        if new_width > 0:
            self.width = new_width

    def set_height(self, new_height):
        if new_height > 0:
            self.height = new_height

 	# Calculate rectangle area, perimeter and diagonal based on "__init__" stored values
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

    # Creates a string thats a picture of the shape based on "__init__" stored values
    # multiplies '*' for width and '*' lines for height
    def get_picture(self):
        line = ''
        if (self.width > 50) or (self.height > 50):
            return "Too big for picture."
        else:
            pic = '*' * self.width
            for n in range(0, self.height):
                line = pic + "\n" + line
            return line

    # Calculates how much of a determined shape fits in the rectangle
    # loops and count iterations [(area of rectangle) - (shape area)] while it's a natural number
    def get_amount_inside(self, shape):
        areax = shape.get_area()
        areay = self.get_area()
        amount = 0
        while areay >= areax:
            areay = areay - areax
            amount = amount + 1
        return amount


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side
