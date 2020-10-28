'''
Exercise: Write a version of the chaos programme for each of the following ways 
of doing the computation. Have your modified programmes pring out 100 iterations 
of the calculation and compare the results when run on the same input.
'''
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100):
        x = 3.9 * x - 3.9 * x * x
        print(x)
        
main()

# The first results are the same as in chaos5.py, but then there are divergencies 
# that grow with each iteration at a faster pace than in chaos6.py