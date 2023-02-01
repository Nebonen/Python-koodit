kaupungit = []

for i in range(5):
    kaupunki = input('Anna kaupungin nimi: ')
    kaupungit.append(kaupunki)
    if i == 5:
        break

for n in kaupungit:
    print(n)
