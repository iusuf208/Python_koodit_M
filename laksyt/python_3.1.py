kuha = float(input("Anna kuhan pituus: "))

pituus = 37

if kuha <= 36:
    print(F"Kuhan pituus on pienempi kuin 37 cm sinun pitää laskea kuhan takaisin järveen, sallittuun pituuden ei riitä vielä {pituus - kuha}")
if kuha >= 37:
    print(F"Kuha on 37 cm pituinen")