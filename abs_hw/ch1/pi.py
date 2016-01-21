print('Enter a radius (in inches) to find the area of a circle:')
r = input()
import math
area = math.pi*int(r)**2
print(str(round(area, 1)) + ' inches squared')
