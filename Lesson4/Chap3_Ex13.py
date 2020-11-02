def main():
    print("This program will calculate the sum of a series of numbers entered by the user")
    n = int(input("Enter the total of numbers to be summed: "))
    total = 0
    for i in range(n):
        number = int(input("Enter a number: "))
        total = number + total
    print("The sum is", total)

main()