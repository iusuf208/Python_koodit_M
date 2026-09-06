import random

def heita(tahkot):
    return random.randint(1,tahkot)

tahkojen_maara = int(input("Anna nopan tahkojen määrä: "))

silmaluku = 0

while silmaluku != tahkojen_maara:
    silmaluku = heita(tahkojen_maara)
    print(silmaluku)