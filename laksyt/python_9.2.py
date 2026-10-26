class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        # Nopeus ei saa ylittää huippunopeutta eikä laskea alle nollan
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0


if __name__ == "__main__":
    autoni = Auto("ABC-123", 142)

    autoni.kiihdytä(30)
    autoni.kiihdytä(70)
    autoni.kiihdytä(50)
    print(f"Nopeus kiihdytysten jälkeen: {autoni.nopeus} km/h")

    autoni.kiihdytä(-200)
    print(f"Nopeus hätäjarrutuksen jälkeen: {autoni.nopeus} km/h")