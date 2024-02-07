import math

class Point:
    def __init__(var, x, y):
        var.x = x
        var.y = y

    def show(var):
        print({var.x}, {var.y})

    def move(var, new_x, new_y):
        var.x = new_x
        var.y = new_y

    def dist(var, other_point):
        dx = var.x - other_point.x
        dy = var.y - other_point.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance

point1 = Point(1, 2)
point2 = Point(4, 6)

point1.show()
point2.show()

distance = point1.dist(point2)
print(distance)

point1.move(3, 5)
point1.show()