steder = []
klesplagg = []
avreisedatoer = []

for i in range(5):
    reisemål = input("Skriv inn dine fem reisemål: ")
    steder.append(reisemål)

for i in range(5):
    klær = input("Skriv inn dine fem plagg: ")
    klesplagg.append(klær)

for i in range(5):
    reiser = input("Skriv inn dine fem avreisedatoer: ")
    avreisedatoer.append(reiser)


reiseplan = [steder, klesplagg, avreisedatoer]

for i in reiseplan:
    print(i)


i1 = int(input("Skriv inn plass: "))

i2 = int(input("Skriv inn plass i plass: "))


if i1 in range(-5, 5) and i2 in range(-5, 5):
    print(reiseplan[i1][i2])

else:
    print("Ugyldig input")

