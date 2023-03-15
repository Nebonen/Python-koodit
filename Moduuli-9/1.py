class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0
    
    def kulje(self, tuntimäärä):
        self.kuljettumatka = self.kuljettumatka + self.nopeus * tuntimäärä

   
auto = Auto('ABS-123', '142 km/h')
print(f'Auton rekisteritunnus on {auto.rekisteritunnus}, huippunopeus on {auto.huippunopeus}, nopeus on {auto.nopeus} km/h ja kuljettu matka on {auto.kuljettumatka}')
auto.kulje(2)
print(f'Auton kuljettu matka on {auto.kuljettumatka} km')