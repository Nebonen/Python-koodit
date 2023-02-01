luvut = []

luku = input('Anna luku, tyhjä lopettaa: ')
while luku != '':
    luku = int(luku)
    luvut.append(luku)
    luku = input('Anna luku, tyhjä lopettaa: ')

luvut.sort(reverse=True)
for i in range(5):
    print(luvut[i])
