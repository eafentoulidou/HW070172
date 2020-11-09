def main ():
    print ("This program encodes and decodes Caesar ciphers. \n")
    text = input("Enter the text you want to encode: ")
    key = int(input("Enter key: "))
    textNew = " "
    for ch in text:
        textNew = chr(ord(ch)+key) + textNew

    print(textNew)

    textRecovered = " "
    for ch in textNew:
        textRecovered = chr(ord(ch)-key) + textRecovered
    
    print(textRecovered)

main()