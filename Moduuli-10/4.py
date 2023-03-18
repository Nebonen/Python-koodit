import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0
    
    def kiihdyta(self, nopeudenmuutos):
        if nopeudenmuutos < 0:
            self.nopeus = self.nopeus - abs(nopeudenmuutos)

        if nopeudenmuutos > 0:
            self.nopeus = self.nopeus + nopeudenmuutos

        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tuntimäärä):
        self.kuljettumatka = self.kuljettumatka + self.nopeus * tuntimäärä

    def __repr__(self):
        return f'{self.rekisteritunnus}, huippunopeus: {self.huippunopeus}, nopeus: {self.nopeus}, kuljettu matka: {self.kuljettumatka}'
    
class Kilpailu:
    def __init__(self, kilpailu_nimi, kilpailu_pituus, osallistuvat_autot):
        self.kilpailun_nimi = kilpailu_nimi
        self.kilpailu_pituus = kilpailu_pituus
        self.osallistuvat_autot = osallistuvat_autot

    def tunti_kuluu(self):
        for auto in self.osallistuvat_autot:
            nopeudenmuutos = random.randint(-10, 15)
            auto.kiihdyta(nopeudenmuutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f'{"Rekisterinumero":<15} {"Nopeus (km/h)":<15} {"Kuljettu matka (km)":<20}')
        for auto in self.osallistuvat_autot:
            print(f'{auto.rekisteritunnus:<15} {auto.nopeus:<15} {auto.kuljettumatka:<20}')

    def kilpailu_ohi(self):
        for auto in self.osallistuvat_autot:
            if auto.kuljettumatka >= self.kilpailu_pituus:
                return True
            else:
                return False

autot = []
for i in range(10):
    rekisteritunnus = 'ABC-' + str(i+1)
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)

kilpailu = Kilpailu('Suuri romuralli', 8000, autot)

tunnit = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit += 1
    if tunnit % 10 == 0:
        print(f'\nTilanne {tunnit} tunnin jälkeen:')
        kilpailu.tulosta_tilanne()

print('\nKilpailu päättynyt!')
print('Tässä tilanne:')
kilpailu.tulosta_tilanne()
