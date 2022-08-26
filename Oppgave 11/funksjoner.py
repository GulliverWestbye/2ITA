import collections

def adder (tall1, tall2):
    return tall1 + tall2

def a():
    tall1 = int(input("Skriv inn tall: "))
    tall2 = int(input("Skriv inn tall: "))
    print(adder(tall1, tall2))

a()
a()


minTekst = input("Skriv inn tekst: ")
minBokstav = input("Skriv inn den bokstaven du vil se hvor mange det er av i teksten du skrev: ")
    

def tellForekomst (minTekst, minBokstav):
    tell = collections.Counter(minTekst)
    return tell[minBokstav]

print(tellForekomst(minTekst, minBokstav))