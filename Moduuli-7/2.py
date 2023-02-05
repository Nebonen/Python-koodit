nimet = set()

nimi = input('Anna nimi: ')
if nimi in nimet:
        print('Aiemmin syötetty nimi.')
elif nimi not in nimet:
        print('Uusi nimi.')
        nimet.add(nimi)

while nimi != '':
    nimi = input('Anna nimi, tyhjä lopettaa: ')
    if nimi in nimet:
        print('Aiemmin syötetty nimi.')
    elif nimi not in nimet:
        print('Uusi nimi.')
        nimet.add(nimi)

for i in nimet:
      print(i)
