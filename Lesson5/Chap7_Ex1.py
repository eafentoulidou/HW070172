def main():
    print("This program will calculate the total wages for a week. \n")
    hours = float(input("Enter the total of hours worked: "))
    rate = float(input("Enter the hourly rate in €: "))
    
    if hours <= 40:
        total = hours * rate
    else:
        total = 40 * rate + (hours-40)*rate*1.5
    
    print("The total wage for the week is", total, "€")

main()