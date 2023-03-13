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

autot = []
for i in range(10):
    rekisteritunnus = 'ABC-' + str(i+1)
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)

voittaja = None
while voittaja == None:
    for auto in autot:
        nopeudenmuutos = random.randint(-10, 15)
        auto.kiihdyta(nopeudenmuutos)
        auto.kulje(1)

        if auto.kuljettumatka >= 10000 and voittaja == None:
            voittaja = auto

print(f'Kilpailun voitti {voittaja.rekisteritunnus}!')

for i in autot:
    print(i)