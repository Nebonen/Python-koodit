import random

nopat = int(input('Anna arpakuutioiden lukumäärä: '))
summa = 0

for i in range(0, nopat):
    summa += random.randint(1,6)
print(summa)
