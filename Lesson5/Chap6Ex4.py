def sumN(n):
    totalN = 0
    for num in range(n+1):
        totalN = num + totalN
    return totalN

def sumNCubes(n):
    totalNCubes = 0
    for num in range(n+1):
        totalNCubes = num*num*num + totalNCubes
    return totalNCubes

number = int(input("Enter a number: "))
ttlN = sumN(number)
ttlNNN = sumNCubes(number)
print("The sum of the first", number, "natural numbers is", ttlN, "and the sum of their cubes is", ttlNNN)