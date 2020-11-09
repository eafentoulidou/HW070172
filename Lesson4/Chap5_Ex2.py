def main():
    print("This program will return the 5-point quiz score as grade")
    points = int(input("Enter the points (0-5): "))
    grades = ["F", "F", "D", "C", "B", "A"]
    points = grades[points]
    print("The grade is {0}".format(points))    
main()