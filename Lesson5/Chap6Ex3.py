import math
def sphereArea(x):
    area = 4 * math.pi * x * x
    return area

radius = input("Enter the radius in cm: ")
Area = sphereArea(float(radius))
print("The surface area of a sphere with radius", radius, "is", Area, "cm2")
