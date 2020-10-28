def main():
    print("This program will compute temperatures from Celsius to Fahrenheit")
    for celsius in range(0, 100, 10):
        fahrenheit = 9/5 * celsius + 32
        print(celsius, "degrees Celsius equals to", fahrenheit, "degrees Fahrenheit")

main()