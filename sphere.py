''' A program that computes various properties of a sphere '''
#There is no pi in python
import math
r = float(input('Radius? '))
D = 2 * r
C = 2 * math.pi * r
A = 4 * math.pi * r ** 2
V = (4/3) * math.pi * r ** 3
print ('Diameter:', D, 'Circumference:', C, 'Area:', A, 'Volume:', V)

