# The python interpreter will not run anything following a "#"
# as code!

# We can use it to add comments to our code so users 
# understand it more easily!

'''
Sometimes comments take up multiple lines.

Three single quotation marks let us type multi-line comments!
'''
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1-x)
        print(x)

main()