def main():
    print("This program will convert any Celsius temperature to Fahrenheit")
    for i in range(5):
        celsius = eval (input("What is the Celsius temerature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is" , fahrenheit, "degrees Fahrenheit.")
    input("Press the <Enter> key to quit")

main()