
class UkuranSepatu():
    Ukuran41 = 20
    Ukuran42 = 40
    Ukuran30 = 80

    def turun(self, x):
        if x <= self.ukuran42:
            return 0
        elif x >= self.ukuran41:
            return 1
        else:
            return bawah(x, self.ukuran41, self.ukuran42)

    def pas(self, x):
        if self.ukuran42 < x < self.ukuran41:
            return atas(x, self.ukuran42, self.ukuran41)
        elif self.ukuran41 < x < self.ukuran30:
            return bawah(x, self.ukuran41, self.ukuran30)
        elif x == self.ukuran41:
            return 1
        else:
            return 0

    def naik(self, x):
        if x >= self.ukuran41:
            return 1
        elif x <= self.ukuran30:
            return 0
        else:
            return up(x, self.ukuran30, self.ukuran41)

class MerkSepatu():
    nike = 30
    adidas = 50
    converse = 70

    def sedikit(self, x):
        if x >= self.adidas:
            return 0
        elif x <= self.nike:
            return 1
        else:
            return down(x, self.nike, self.adidas)
    
    def cukup(self, x):
        if self.adidas < x < self.nike:
            return up(x, self.adidas, self.nike)
        elif self.nike < x < self.converse:
            return down(x, self.nike, self.converse)
        elif x == self.nike:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.converse:
            return 1
        elif x <= self.nike:
            return 0
        else:
            return up(x, self.nike, self.converse)

class WarnaSepatu():
    putih = 30
    hitam = 40
    navy = 50

    def sedikit(self, x):
        if x >= self.hitam:
            return 0
        elif x <= self.putih:
            return 1
        else:
            return down(x, self.putih, self.hitam)
    
    def cukup(self, x):
        if self.putih < x < self.hitam:
            return up(x, self.hitam, self.putih)
        elif self.putih < x < self.navy:
            return down(x, self.putih, self.navy)
        elif x == self.putih:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.navy:
            return 1
        elif x <= self.putih:
            return 0
        else:
            return up(x, self.putih, self.pink)

class MotifSepatu():
    batik = 10
    bunga = 20
    kartun = 30
   
    def sedikit(self, x):
        if x >= self.bunga:
            return 0
        elif x <= self.batik:
            return 1
        else:
            return down(x, self.batik, self.bunga)
    
    def cukup(self, x):
        if self.batik < x < self.bunga:
            return up(x, self.batik, self.)
        elif self.batik < x < self.kartun:
            return down(x, self.bunga, self.kartun)
        elif x == self.bunga:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.kartun:
            return 1
        elif x <= self.bunga:
            return 0
        else:
            return up(x, self.bunga, self.kartun)
