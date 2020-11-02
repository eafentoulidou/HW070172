import math
def main():
    print("This program will calculate the area of a triangle")
    a = int(input("Enter the length of the side a: "))
    b = int(input("Enter the length of the side b: "))
    c = int(input("Enter the length of the side c: "))
    s = (a + b + c) / 2
    A = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print("The area of a triangle with side length", a, b, c, "is", A)
main()