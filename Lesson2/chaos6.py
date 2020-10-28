'''
Exercise: Write a version of the chaos programme for each of the following ways 
of doing the computation. Have your modified programmes pring out 100 iterations 
of the calculation and compare the results when run on the same input.
'''
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100):
        x = 3.9 * (x - x * x)
        print(x)
        
main()

# The results are slightly different than in chaos5.py in the first iteration, 
# and the gap becomes bigger with every iteration.