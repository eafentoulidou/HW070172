import math
def main():
    print("This program will approximate the value of pi")
    n = int(input("Enter the total of numbers to be summed: "))
    total = 0
    factor = 4
    for num in range(1, n*2, 2):
        total = total + factor/num
        factor = -factor
    print("pi is approximately", total)
    compare = math.pi - total
    print("The difference between my calculation and pi is", compare)

main()