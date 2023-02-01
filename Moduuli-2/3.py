kanta = input('Anna kanta: ')
korkeus = input('Anna korkeus: ')

kantanum = float(kanta)
korkeusnum = float(korkeus)

pintaala = kantanum * korkeusnum
piiri = kantanum * 2 + korkeusnum * 2

print('Pinta-ala on ' + str(pintaala))
print('Piiri on ' + str(piiri))