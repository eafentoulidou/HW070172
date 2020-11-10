def main():
    print("This program will return the 5-point quiz score as grade")
    points = int(input("Enter the points (0-5): "))
    grades = ["F", "D", "C", "B", "A"]
    if points <= 1:
         grade = grades[0]
    elif points == 2:
         grade = grades[1]
    elif points == 3:
         grade = grades[2]
    elif points == 4:
         grade = grades[3]
    else:
         grade = grades[4]
    print("The grade is {0}".format(grade))    
main()