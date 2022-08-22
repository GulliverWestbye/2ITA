def riktig():
    print("Riktig rekkefølge!")

def feil():
    print("Feil rekkefølge!")

dato = input(f"Skriv inn dato: ")
måned = input(f"skriv inn måned: ")

dato2 = input(f"Skriv inn din andre dato: ")
måned2 = input(f"Skriv inn din andre måned: ")

if måned < måned2:
    riktig()

elif måned > måned2:
    feil()

elif måned == måned2:
    if dato < dato2:
        riktig()
    elif dato > dato2:
        feil()
    elif dato == dato2:
        print("Samme dato!")

   