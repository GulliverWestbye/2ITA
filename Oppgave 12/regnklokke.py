
liste = []


tall = ""
while tall != "0":
    tall = input("Skriv inn tall (0=stop): ")
    liste.append(int(tall))

for i in liste:
    print(i)

minSum = 0

for i in liste:
    minSum += i

print(minSum)

sjekk = 0
for i in liste:
    if sjekk == 0:
        sjekk = 1
        minst = i
    elif i < minst:
        minst = i
print(f"{minst} er det minste tallet i listen.")

sjekk = 0
for i in liste:
    if sjekk == 0:
        sjekk = 1
        størst = i
    elif i > størst:
        størst = i
print(f"{størst} er det største tallet i listen.")