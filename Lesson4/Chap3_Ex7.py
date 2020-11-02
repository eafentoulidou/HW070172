import math
def main():
    print("This program will calculate the distance between two points")
    x1 = float(input("Enter the coordinate x for point 1: "))
    y1 = float(input("Enter the coordinate y for point 1: "))
    x2 = float(input("Enter the coordinate x for point 2: "))
    y2 = float(input("Enter the coordinate y for point 2: "))
    distance = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
    print("The distance between points", x1, "*", y1, "and", x2, "*", y2, "is", distance)
main()