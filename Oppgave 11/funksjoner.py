import collections

def adder (tall1, tall2):
    return tall1 + tall2

def a():
    tall1 = int(input("Skriv inn tall: "))
    tall2 = int(input("Skriv inn tall: "))
    print(adder(tall1, tall2))

a()
a()


tekst = input("Skriv inn tekst: ")
bokstav = input("Skriv inn den bokstaven du vil se hvor mange det er av i teksten du skrev: ")

tell = collections.Counter(tekst)

print(tell[bokstav])
