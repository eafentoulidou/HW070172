import math
def main():
    print("This program will calculate the cost per square inch of a circular pizza given its diameter and price")
    diameter = float(input("Diameter in inches: "))
    price = float(input("Total price of pizza: "))
    radius = diameter / 2
    area = math.pi * radius * radius
    Total = price / area
    print("The cost of a pizza that costs", price, "dollars 1with a diameter of", diameter, "inches is", Total,
    "dollars per inch2")
main()