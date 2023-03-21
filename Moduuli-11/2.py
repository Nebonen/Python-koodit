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

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankinkoko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankinkoko = bensatankinkoko

sahkoauto = Sahkoauto('ABC-123', 180, 52.5)
polttomoottoriauto = Polttomoottoriauto('ABD-123', 165, 32.3)
sahkoauto.kiihdyta(100)
polttomoottoriauto.kiihdyta(80)
sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f'Sähkoauton mittarilukema on {sahkoauto.kuljettumatka} km')
print(f'Polttomoottoriauton mittarilukema on {polttomoottoriauto.kuljettumatka} km')