class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros < self.alin_kerros:
            kohde_kerros = self.alin_kerros
        elif kohde_kerros > self.ylin_kerros:
            kohde_kerros = self.ylin_kerros

        while self.nykyinen_kerros != kohde_kerros:
            if self.nykyinen_kerros < kohde_kerros:
                self.kerros_ylos()
            else:
                self.kerros_alas()

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f'Hissi on nyt kerroksessa {self.nykyinen_kerros}')

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f'Hissi on nyt kerroksessa {self.nykyinen_kerros}')

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_maara = hissien_maara
        self.hissit = [Hissi(alin_kerros, ylin_kerros)for i in range(hissien_maara)]
    
    def aja_hissia(self, hissin_numero, kohde_kerros):
        hissi = self.hissit[hissin_numero - 1]
        hissi.siirry_kerrokseen(kohde_kerros)
        hissi.siirry_kerrokseen(self.alin_kerros)
    
    def palohalytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(hissi.alin_kerros)
        print('Palohälytys!')
        print('Hissit ovat nyt alimmassa kerroksessa')


talo = Talo(1, 10, 2)
talo.aja_hissia(1, 5)
talo.aja_hissia(2, 9)
talo.palohalytys()