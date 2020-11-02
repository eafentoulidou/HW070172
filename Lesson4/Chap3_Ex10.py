import math
def main():
    print("This program will calculate the length of a ladder required to reach a given height when leaned against a house.")
    height = int(input("Enter the height you want to reach in cm: "))
    degrees = int(input("Enter the angle of the leaning ladder in degrees: "))
    radians = math.pi * degrees / 180
    length = height / math.sin(radians)
    print("The length of the ladder must be", length, "cm")
main()