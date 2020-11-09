def main ():
    print ("This program calculates the numeric value of a name. \n")
    first = input("Enter your first name: ")
    number = 0

    for ch in first:
        number = ord(ch) + number
    
    print(number)
main()