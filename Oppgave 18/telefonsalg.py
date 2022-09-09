salg = {}

def innlesing(filnavn):
    tekstfil = open(f"{filnavn}", "r")
    tekstfil_alle_verdier = tekstfil.readlines()
    for i in tekstfil_alle_verdier:
        salg[i.split()[0]] = int(i.split()[1])
    return salg

def maanedsSalgperson():
    mestSalg = 0
    for i in salg:
        if salg[i] > mestSalg:
            mestSalg = salg[i]
            Person = i
    print(f"{Person} hadde mest salg med {mestSalg} kr")

def totalAntallSalg():
    global total
    total = 0
    for i in salg:
        total += salg[i]
    print(f"Totalt antall salg var {total} kr")

def gjennomsnittligSalg():
    total = 0
    for i in salg:
        total += salg[i]
    print(f"Gjennomsnittlig salg var {total/len(salg)} kr")

def hovedprogram():
    print(innlesing("Oppgave 18/salgstall.txt"))
    maanedsSalgperson()
    totalAntallSalg()
    gjennomsnittligSalg()
    for i in salg:
        print(i)

hovedprogram()