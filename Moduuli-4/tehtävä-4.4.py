import random

numero = random.randint(1,10)
while True:
    arvaus = int(input('Anna arvaus: '))
    if arvaus > numero:
        print('Liian suuri arvaus')
    elif arvaus < numero:
        print('Liian pieni arvaus')
    elif arvaus == numero:
        print('Oikein')
        break
