def main():
    print("This program calculates the future value")
    print("of an investment over a period of n years")

    principal = eval(input("Enter the initial principal "))
    apr = eval(input("Enter the annual interest rate: "))
    n = eval(input("Enter the number of years: "))

    for i in range(n):
        principal = principal * (1 + apr)

    print("The value in", n, "years is", principal)

main()