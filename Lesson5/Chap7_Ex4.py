def main():
    print("This program will classify students according to credits earned.")
    nrCredits = int(input("Enter the number of credits: "))
    statuses = ["Freshman", "Sophomore", "Junior", "Senior"]
    if nrCredits < 7:
         status = statuses[0]
    elif nrCredits <= 15:
         status = statuses[1]
    elif nrCredits <= 25:
         status = statuses[2]
    elif nrCredits >= 26:
         status = statuses[3]
    print("For {0} credits the status is {1}".format(nrCredits, status))    
main()