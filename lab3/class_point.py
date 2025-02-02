import math

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def show(self):
        print("Coordinates: (" + str(self.x) + ", " + str(self.y) + ")")
    def move(self, upd_x, upd_y):
        self.x = upd_x
        self.y = upd_y
    def dist(self, second_point):
        distance = math.sqrt((self.x - second_point.x)**2 + (self.y - second_point.y)**2)
        print(round(distance, 4))
    
x1 = float(input("X1 = "))
y1 = float(input("Y1 = "))
point1 = Point(x1, y1)
x2 = float(input("X2 = "))
y2 = float(input("Y2 = "))
point2 = Point(x2, y2)

point1.show()
point2.show()
point1.dist(point2)
point2.move(4, 3)
point1.dist(point2)
