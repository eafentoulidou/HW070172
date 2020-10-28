'''
Sometimes comments take up multiple lines.

Three single quotation marks let us type multi-line comments!
'''
# Exercise 2: Modify the chaos programme using 2.0 instead of 3.9
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0 * x * (1-x)
        print(x)

main()

# Other than chaos.py, here the last three iterations always have .5