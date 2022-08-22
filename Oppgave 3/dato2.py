def riktig():
    print("Riktig rekkefølge!")

def feil():
    print("Feil rekkefølge!")


dato = input(f"Skriv in dato med måned (eksmpel 2412)")

dato2 = input(f"Skriv in dato med måned (eksmpel 2412)")


try:
    int(dato)
    int(dato2)
except ValueError:
    print("Dette er feil format.")
    exit()


if int(dato[0]) < int(dato2[0]) and int(dato[1]) < int(dato2[1]):
    riktig()
