tuumat = float(input("Anna tuumamäärä (negatiivinen luku lopettaa: "))

while tuumat >= 0:
    senttim = tuumat * 2.54
    print(f"{tuumat} tuuma on {senttim:.2f} cm\n")
    tuumat = float(input("Anna tuumamäärä (negatiivinen luku lopettaa: "))

print("Ohjelma lopetettu.")