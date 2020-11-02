def main():
    print("This program will calculate the average of a series of numbers entered by the user")
    n = int(input("Enter the total of numbers, the average of which should be found: "))
    total = 0
    for i in range(n):
        number = int(input("Enter a number: "))
        total = number + total
    average = total / n
    print("The average is", average)

main()