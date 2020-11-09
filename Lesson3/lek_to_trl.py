def main():
    print("This program will convert Albanian lek to Turkish lira") 
    lek = eval (input("Enter the amount in Albanian lek: "))
    date =input("Enter current date: ")
    rate = eval (input("Enter today's exchange rate from lek to trl: "))
    trl =  lek * rate
    if lek == 1:
        print("On", date, lek, "Albanian lek amounts to", trl, "Turkish lira")
    else:
        print("On", date, lek, "Albanian lek amount to", trl, "Turkish lira")
        
            

main()