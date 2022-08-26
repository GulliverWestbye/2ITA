from typing import Dict


Dict = {"melk": 14.90, "brød": 24.90, "yoghurt": 12.90, "pizza": 39.90}

for i in range (2):
    vare = input("legg inn vare: ")
    pris = input("legg inn pris på vare: ")

    try:
        int(pris)
    except ValueError:
        exit()
        
    Dict[vare] = int(pris)

print(Dict)
