print("Hello Verden!")

dittnavn = input("Skriv inn ditt navn: ")
print(f"hei {dittnavn}")


a = 1
b = 2
print(a)
print(b)


differanse = a - b

if type(a) == int and type(b) == int:
    print(differanse)
else:
    exit()


dittnavn2 = input(f"Skriv inn ditt andre navn: ")
dittnavn2kopi = dittnavn2
dittnavn2 = dittnavn + dittnavn2
print(dittnavn2)

dittnavn2 = dittnavn + " og " + dittnavn2kopi
print(dittnavn2)
