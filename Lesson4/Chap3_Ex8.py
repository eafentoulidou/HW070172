import math
def main():
    print("This program will calculate the Gregorian epact for a given year")
    year = int(input("Enter the year: "))
    C = year // 100
    epact = (8 + (C//4) - C + ((8*C + 13)//25) + 11 * (year%19))%30
    print("The Gregorian epact for the year", year, "is", epact)
main()