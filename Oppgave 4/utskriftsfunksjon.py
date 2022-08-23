def hilsen():
    navn = input(f"Skriv inn ditt navn: ")
    sted = input(f"Hvor kommer du fra? ")
    print(f"Hei {navn} du er fra {sted}")

for i in range (3):
    hilsen()