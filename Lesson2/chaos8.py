'''
Exercise: Modify the chaos programme so that it accepts two inputs 
and then prints a table with two columns.
'''
def main():
    print("This program illustrates a chaotic function")
    x, y = eval(input("Enter a number between 0 and 1: "))
    for i in range(100):
        x = 3.9 * x - 3.9 * x * x
        y = 3.9 * y - 3.9 * y * y
        print(x, y)
main()
