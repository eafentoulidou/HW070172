def main():
    print("This program will calculate the cost of an order from the coffee shop Konditorei")
    coffee = float(input("Coffee in pounds: "))
    total = coffee * 10.50 + 0.86 * coffee + 1.50
    print("The total cost of an order for", coffee, "pounds coffee is", total, "dollars")
main()