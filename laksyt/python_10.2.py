
class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerros_ylös(self):
        if self.kerros < self.ylin:
            self.kerros += 1
            print("Hissi on kerroksessa", self.kerros)

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1
            print("Hissi on kerroksessa", self.kerros)

    def siirry_kerrokseen(self, kohde):
        if kohde < self.alin or kohde > self.ylin:
            print("Virheellinen kerros")
            return

        while self.kerros < kohde:
            self.kerros_ylös()

        while self.kerros > kohde:
            self.kerros_alas()


class Talo:
    def __init__(self, alin, ylin, hissien_maara):
        self.hissit = []

        for i in range(hissien_maara):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissiä(self, hissin_numero, kohde):
        print("Hissi", hissin_numero, "liikkuu:")
        self.hissit[hissin_numero - 1].siirry_kerrokseen(kohde)


# Pääohjelma
talo = Talo(1, 10, 3)

talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 7)
talo.aja_hissiä(3, 4)
talo.aja_hissiä(1, 1)
