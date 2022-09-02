mineOrd = []

def slaasammen():
    ord1 = input("Skriv inn et ord: ")
    ord2 = input("Skriv inn et ord: ")
    ordsammen = ord1 + ord2
    print(ordsammen)


def skrivUT():
    for i in range(5):
        nyting = input("Skriv inn et ord: ")
        mineOrd.append(nyting)

    for i in mineOrd:
        print(i)

kul = input("")
while kul != "s":
    kul = input("Skriv inn i for slå sammen ord, skriv u for kul prosedyre, skriv s for å avslutte: ")

    if kul == "i":
        slaasammen()
    
    elif kul == "u":
        skrivUT()

    elif kul != "s":
        print("Ugyldig input")
        break
