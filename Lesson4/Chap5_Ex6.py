def main ():
    print ("This program calculates the numeric value of a name. \n")
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    name = first+last
    number = 0

    for ch in name:
        number = ord(ch) + number
    
    print(number)
main()