kuhanpituus = int(input('anna kuhan pituus senttimetreinä: '))
puuttuu = 37 - kuhanpituus

if kuhanpituus < 37:
    print('Kuha on alamittainen, pituudesta puuttuu ' + str(puuttuu) + '. Tiputa takaisin järveen.')
else:
    print('Kuha on sopivan kokoinen')
    