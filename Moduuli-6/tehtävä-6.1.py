import random

def heita_noppaa():
    luku = 0
    print('Heitetään noppaa kunnes silmäluku on 6:')
    while luku != 6:
        luku = random.randint(1,6)
        print(luku)

heita_noppaa()
