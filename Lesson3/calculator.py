def main():
    print("This program will perform calculations of your choice")
    x = eval(input("Enter a mathematical expression "))
    for i in range(0, 100, 10):
        y = x
        print(x, "=", y)
    input()
main()
