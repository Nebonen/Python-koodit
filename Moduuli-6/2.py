import random

def heita_noppaa(tahkot):
    luku = 0
    print(f'Heitetään noppaa kunnes silmäluku on {tahkot}:')
    while luku != tahkot:
        luku = random.randint(1,tahkot)
        print(luku)

tahkot = int(input('Mikä on nopan maksimisilmäluku? '))
heita_noppaa(tahkot)
