import random

sala_luku = random.randint(1,10)

arvaus = int(input("Arvaa luku väliltä 1-10: "))

while arvaus != sala_luku:
    if arvaus > sala_luku:
        print("Liian suuri arvaus")
    else:
        print("Liian pieni arvaus")

    arvaus = int(input("Arvaa uudelleen: "))

print("Oikein")