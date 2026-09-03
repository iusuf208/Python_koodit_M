import random

def heita():
    return random.randint(1,6)

silmaluku = 0

while silmaluku != 6:
    silmaluku = heita()
    print(silmaluku)
