lentokentat = {}

while True:
    print('Mitä haluat tehdä?:')
    print('1. Syötä uuden lentoaseman tiedot')
    print('2. Hae lentoaseman tiedot')
    print('3. Lopeta')
    valinta = int(input('Valitsemasi toiminto: '))

    if valinta == 1:
        icao_koodi = input('Syötä ICAO-koodi: ')
        nimi = input('Syötä lentoaseman nimi: ')
        lentokentat[icao_koodi] = nimi
    elif valinta == 2:
        icao_koodi = input('Syötä haettava ICAO-koodi: ')
        if icao_koodi in lentokentat:
            print(f'Lentoasema on {lentokentat[icao_koodi]}.')
        else:
            print('Lentoasemaa ei löytynyt.')
    elif valinta == 3:
        break
