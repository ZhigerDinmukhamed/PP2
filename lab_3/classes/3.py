class Rectangle:
    def __init__(var, length, width):
        var.length = length
        var.width = width

    def compute_area(var):
        return var.length * var.width

rectangle = Rectangle(4, 6)
print(rectangle.compute_area())