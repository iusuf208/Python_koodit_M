oikea_tunnus = "python"
oikea_salasana = "rules"

yritykset = 0
kirjautunut = False

while yritykset < 5 and not kirjautunut:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        kirjautunut = True
    else:
        yritykset += 1
        if yritykset < 5:
            print(f"Väärä tunnus tai salasana. Yrityksiä jäljellä: {5 - yritykset}\n")
if kirjautunut:
    print("Tervettuloa!")
else:
    print("Pääsy evätty")