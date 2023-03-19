class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f'Nimi: {self.nimi}')

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        Julkaisu.__init__(self, nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
    
    def tulosta_tiedot(self):
        Julkaisu.tulosta_tiedot(self)
        print(f'Kirjoittaja: {self.kirjoittaja}')
        print(f'Sivumaara: {self.sivumaara}')

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        Julkaisu.__init__(self, nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        Julkaisu.tulosta_tiedot(self)
        print(f'Päätoimittaja: {self.paatoimittaja}')

lehti = Lehti('Aku Ankka', 'Aki Hyyppä')
kirja = Kirja('Hytti n:0 6', 'Rosa Liksom', 200)

print('Lehden tiedot:')
lehti.tulosta_tiedot()
print('\nKirjan tiedot:')
kirja.tulosta_tiedot()