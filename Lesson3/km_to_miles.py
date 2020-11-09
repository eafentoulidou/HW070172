def main():
    print("This program will convert kilometers to miles") 
    km = eval (input("Enter the distance in kilometers: "))
    miles =  km * .62
    if km == 1:
        print(km, "kilometer is", miles, "miles")
    else:
        print(km, "kilometers are", miles, "miles")

main()