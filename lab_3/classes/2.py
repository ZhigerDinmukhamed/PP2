class Shape:
    def area(var):
        return 0

class Square(Shape):
    def __init__(var, length):
        var.length = length

    def area(var):
        return var.length **2

shape = Shape()
print(shape.area())

square = Square(5)
print(square.area())