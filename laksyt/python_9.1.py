class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

if __name__ == "__main__":
    autoni = Auto("ABC-123", 142)
    print(f"Auto: {autoni.rekisteritunnus}, Huippunopeus: {autoni.huippunopeus} km/h, "
          f"Nopeus: {autoni.nopeus} km/h, Kuljettu matka: {autoni.kuljettu_matka} km")