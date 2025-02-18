import math

sides = float(input('Input number of sides: '))
length = float(input('Input the length of a side: '))
area = 0.5 * sides * length * (length / (2 * math.tan(math.pi/sides)))
print('The area of the polygon is: ', round(area, 2))