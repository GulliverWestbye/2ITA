tall = [2, 7, 3]
tall.append(9)

print(tall[0])
print(tall[2])

addisjon = 0
for i in tall:
    addisjon += i

multi = 1
for i in tall:
    multi *= i

print(addisjon)
print(multi)

tall2 = [addisjon, multi]

tall3 = [tall, tall2]

print(tall3)

tall3.pop