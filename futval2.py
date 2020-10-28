def main():
    print("This program calculates the future value")
    print("of an investment over a period of n years, when the interest is accrued in n periods")

    principal = eval(input("Enter the initial principal "))
    rate = eval(input("Enter the period interest rate: "))
    periods = eval(input("Enter the number of times that the interest is compounded per yr: "))
    years = eval(input("Enter the number of years: "))

    for i in range(periods * years):
        principal = principal * (1 + rate)

    print("The value in", years, "years is", principal)

main()