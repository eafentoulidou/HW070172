def main():
    weight = float(input("Enter the weight in pounds: "))
    height = float(input("Enter the height in inches: "))

    BMI = weight*720/(height**2)

    if BMI < 19:
        print("The BMI is", BMI, "and this is too low.")
    elif BMI >= 19 and BMI <= 25:
        print("The BMI is", BMI, "and this is healthy.")
    else:
        print("The BMI is", BMI, "and this is too high.")

main()