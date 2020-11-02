def main():
    print("This program will calculate the slope of a line through two non-vertical points")
    x1 = float(input("Enter the coordinate x for point 1: "))
    y1 = float(input("Enter the coordinate y for point 1: "))
    x2 = float(input("Enter the coordinate x for point 2: "))
    y2 = float(input("Enter the coordinate y for point 2: "))
    slope = (y2 -y1) / (x2-x1)
    print("The slope of a line through points", x1, "*", y1, "and", x2, "*", y2, "is", slope, "%")
main()