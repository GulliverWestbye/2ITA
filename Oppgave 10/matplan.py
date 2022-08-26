from typing import Dict


Dict = {"Per Hansen": ["grøt", "burger", "våruller"], "Idun Ibsen": ["brød", "pasta", "rundstykker"], "Ole Flesvold": ["egg", "suppe", "toast"]}

for i in Dict:
    print(i)

navn = input("Skriv inn navn til beboer: ")

if navn in Dict:
    for i in Dict:
        if navn == i:
            print(Dict[i][0])
            print(Dict[i][1])
            print(Dict[i][2])

else:
    print("navn er ikke i listen")