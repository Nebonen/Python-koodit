vuosiluku = int(input('Anna vuosiluku: '))

if (vuosiluku % 400 == 0) and (vuosiluku % 100 == 0):
    print('vuosi on karkausvuosi')
elif (vuosiluku % 4 == 0) and (vuosiluku % 100 != 0):
    print('Vuosi on karkausvuosi')
else:
    print('Vuosi ei ole karkausvuosi')