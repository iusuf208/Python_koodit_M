
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


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankin_koko = tankin_koko


# Pääohjelma
sahkoauto = Sähköauto("ABC-15", 180, 52.5)
bensaauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.kiihdytä(120)
bensaauto.kiihdytä(100)

sahkoauto.kulje(3)
bensaauto.kulje(3)

print("Sähköauton matka:", sahkoauto.matka, "km")
print("Polttomoottoriauton matka:", bensaauto.matka, "km")
