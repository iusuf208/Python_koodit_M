luvut = []

syote = input("Anna luku (tyhjä lopettaa): ")

while syote != "":
    luku = float(syote)
    luvut.append(luku)
    syote = input("Anna luku (tyhjä lopettaa): )")

luvut.sort(reverse=True)

viisi_suurinta = luvut[:5]

print("\nViisi suurinta lukua suurimmasta alkaen: ")
for luku in viisi_suurinta:
    print(luku)