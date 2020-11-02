def main():
    print("This program will calculate the molecular weight of a carbohydrate in grams per mole")
    molecule = input("Molecule to calculate: ")
    hydrogen = int(input("Number of hydrogen atoms in the molecule: "))
    carbon = int(input("Number of carbon atoms in the molecule: "))
    oxygen = int(input("Number of oxygen atoms in the molecule: "))
    weight = hydrogen * 1.00794 + carbon * 12.0107 + oxygen * 15.9994
    print("The molecular weight of", molecule, "is", weight, "grams per mole")
main()