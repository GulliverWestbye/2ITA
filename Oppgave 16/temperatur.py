årstemp = []

with open('temperatur.txt') as f:
    temperaturer = f.read().splitlines()
    årstemp.append(temperaturer)

def gjennomsnitt():
    sum = 0
    for i in temperaturer:
        sum += int(i)
    print(sum/len(temperaturer))

gjennomsnitt()