import math
def main():
    print("This program will calculate the volume and surface area of a sphere")
    radius = float(input("Radius in cm: "))
    volume = 4/3 * math.pi * radius * radius * radius
    area = 4 * math.pi * radius * radius
    print("The volume of a sphere with a radius of", radius, "cm is", volume,
    "cm3, and its surface area is", area, "cm2.")
main()