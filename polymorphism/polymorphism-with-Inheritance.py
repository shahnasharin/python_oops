#-----------------------Polymorphism with Inheritance:---------------------------------

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

def calculate_area(shape):
    return shape.area()

circle = Circle(5)
square = Square(4)

print(f"Circle Area: {calculate_area(circle)}")  # Output: Circle Area: 78.5
print(f"Square Area: {calculate_area(square)}")  # Output: Square Area: 16
