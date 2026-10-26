class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


if __name__ == "__main__":
    autoni = Auto("ABC-123", 142)

    autoni.nopeus = 60
    autoni.kuljettu_matka = 2000
    autoni.kulje(1.5)
    print(f"Kuljettu matka ajon jälkeen: {autoni.kuljettu_matka} km")