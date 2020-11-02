def main():
    print("This program will determine the distance to a lightning strike based on the time elapsed between the flash and the sound of thunder")
    time = float(input("Time elapsed in sec: "))
    feet = 1100 * time
    miles = feet / 5280
    print("The distance to the lightning strike is", miles, "miles")
main()