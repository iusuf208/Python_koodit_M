import random


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
    autot = []
    for i in range(1, 11):
        rek_tunnus = f"ABC-{i}"
        max_nopeus = random.randint(100, 200)
        autot.append(Auto(rek_tunnus, max_nopeus))

    kilpailu_kayntiin = True
    tunnit = 0

    while kilpailu_kayntiin:
        tunnit += 1
        for auto in autot:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)

            auto.kulje(1)

            if auto.kuljettu_matka >= 10000:
                kilpailu_kayntiin = False

    print(f"\nKilpailu päättyi! Aikaa kului {tunnit} tuntia.\n")
    print(f"{'Rekisteritunnus':<15} | {'Huippunopeus':<13} | {'Nopeus':<10} | {'Kuljettu matka':<15}")
    print("-" * 63)
    for auto in autot:
        print(
            f"{auto.rekisteritunnus:<15} | {auto.huippunopeus:<13} | {auto.nopeus:<10} | {auto.kuljettu_matka:<15.1f}")