def main():
    print("This program will calculate the sum of the first n numbers")
    n = int(input("Enter a number: "))
    total = 0
    for num in range(n+1):
        total = num + total
    print("The sum of the first", n, "numbers is", total)

main()