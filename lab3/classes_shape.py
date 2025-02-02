class Shape:
    def area(self):
        print("Shape's area:" + '0')
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        print("Square's area: " + str(self.length**2))

shape = Shape()
length = int(input("Square's length: "))
square = Square(length)
shape.area()
square.area()

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print("Rectangle's area: " + str(self.length * self.width))
length = int(input("Rectangle's length: "))
width = int(input("Rectangle's width: "))
rec = Rectangle(length, width)
rec.area()