def addisjon(a, b):
    print(f"Legg sammen {a} og {b}: ")
    return a + b

def subtraksjon (a, b):
    print(f"Subtraher {a} og {b}: ")
    return a - b

def divisjon (a, b):
    print(f"Divdser {a} og {b}: ")
    return a / b

def tommerTilCm (antallTommer):
    print(f"Konverter {antallTommer} tommer til cm: ")
    return antallTommer * 2.54

def skrivBeregninger ():
    k1 = input("Skriv inn to tall du vil legge sammen: ")
    k2 = input("Skriv inn to tall du vil legge sammen: ")
    print(addisjon(float(k1), float(k2)))

    k3 = input("Skriv inn to tall du vil subtrahere: ")
    k4 = input("Skriv inn to tall du vil subtrahere: ")
    print(subtraksjon(float(k3), float(k4)))

    k5 = input("Skriv inn to tall du vil dele: ")
    k6 = input("Skriv inn to tall du vil dele: ")
    print(divisjon(float(k5), float(k6)))

    k7 = input("Skriv inn antall tommer du vil konvertere til cm: ")
    print(tommerTilCm(float(k7)))



skrivBeregninger()  