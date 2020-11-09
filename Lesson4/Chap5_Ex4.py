def main():
    print("This program will find the acronym of any phrase. \n")
    
    phrase = input("Enter a phrase: ")
    phrase = phrase.upper()
    words = phrase.split()
    
    acronym = " "
    for word in words:
        acronym = acronym + word[0]
    
    print(acronym)

main()