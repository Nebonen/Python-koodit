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

auto = Auto('ABS-123', 142)
print(f'Auton rekisteritunnus on {auto.rekisteritunnus}, huippunopeus on {auto.huippunopeus} km/h, nopeus on {auto.nopeus} km/h ja kuljettu matka on {auto.kuljettumatka} km')
auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print(f'Auton nopeus on {auto.nopeus} km/h')
auto.kiihdyta(-200)
print('Hätäjarrutus!')
print(f'Auton uusi nopeus on {auto.nopeus} km/h')
auto.kulje(5)
print(f'Auton kuljettu matka on {auto.kuljettumatka} km')
