import random

pisteet = int(input('Kuinka monta pistettä arvotaan? '))
ympyra = 0
laskuri = 0
while laskuri < pisteet:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        ympyra += 1
    laskuri += 1
pii = 4 * ympyra / pisteet
print('Piin likiarvo on ' + str(pii))
