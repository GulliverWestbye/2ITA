def info():
    global alder
    global navn
    alder = int(input("Skriv inn din alder: "))
    navn = input("Skriv inn ditt navn: ")

info()

billettpris = 0

if alder <= 17:
    print(f"Din billettpris er: {billettpris + 30}")

elif alder in range(18,63):
    print(f"Din billettpris er: {billettpris + 50}")

else:
    print(f"Din billettpris er: {billettpris + 35}")