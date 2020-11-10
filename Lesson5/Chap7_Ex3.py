def main():
    print("This program will return the 100-point quiz score as grade")
    points = int(input("Enter the points (0-100): "))
    grades = ["F", "D", "C", "B", "A"]
    if points < 60:
         grade = grades[0]
    elif points < 70:
         grade = grades[1]
    elif points < 80:
         grade = grades[2]
    elif points < 90:
         grade = grades[3]
    elif points <= 100:
         grade = grades[4]
    print("The grade is {0}".format(grade))    
main()