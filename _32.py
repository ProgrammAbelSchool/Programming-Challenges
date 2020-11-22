from math import pi

radius = int(input("enter the radius of a cylinder: "))
depth = int(input("enter the depth of the same cylinder: "))

area = pi * radius**2
volume = area * depth

print(round(volume, 3))