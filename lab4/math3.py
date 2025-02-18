<<<<<<< HEAD
import math

sides = float(input('Input number of sides: '))
length = float(input('Input the length of a side: '))
area = 0.5 * sides * length * (length / (2 * math.tan(math.pi/sides)))
=======
import math

sides = float(input('Input number of sides: '))
length = float(input('Input the length of a side: '))
area = 0.5 * sides * length * (length / (2 * math.tan(math.pi/sides)))
>>>>>>> e8d0fc96cf3dff340827b2be2b410d75d5e2b020
print('The area of the polygon is: ', round(area, 2))