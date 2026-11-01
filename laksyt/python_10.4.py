
import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\n{self.nimi}")
        print(f"{'Auto':<12}{'Huippunopeus':<15}{'Nopeus':<12}{'Matka':<10}")
        print("-" * 49)

        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<12}{auto.huippunopeus:<15}{auto.nopeus:<12}{auto.matka:<10.1f}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False


# Pääohjelma
autot = []

for i in range(1, 11):
    autot.append(Auto("ABC-" + str(i), random.randint(100, 200)))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit += 1

    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()

print("\nKilpailu päättyi!")
print("Kilpailun kesto:", tunnit, "tuntia")

kilpailu.tulosta_tilanne()
