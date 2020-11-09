import math

def fib1(n):
    if n < 3:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

def fib2(n):
    fib = [1, 1]
    fiblen = 2
    while fiblen < n:
        fib.append(fib[fiblen-1] + fib[fiblen-2])
        fiblen = len(fib)
    fib
    return fib[n-1]

def fib3(n):
    sq5 = math.sqrt(5)
    return ((1+sq5)/2)**(n-1) + ((1-sq5)/2)**(n-1)

def main():
    print("This program will calculate the nth Fibonacci number")
    n = int(input("Enter the number of elements in Fibonacci series, n>=2: "))
    f1 = fib1(n)
    f2 = fib2(n)
    f3 = fib3(n)
    print("fib1 " + str(f1))
    print("fib2 " + str(f3))
    print("fib3 " + str(f3))

main()