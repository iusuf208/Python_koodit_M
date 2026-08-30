syote = int(input("Anna luku (Paina Enter, jotta ohjelma pysähtyy): "))

luvut = []

while syote != "":
    luku = int(syote)
    luvut.append(luku)
    syote = input("Anna luku (Paina Enter, jotta ohjelma): ")

if luvut:
    print(f"Pienin luku: {min(luvut)}")
    print(f"Pienin luku: {max(luvut)}")
else:
    print("Et syöttänyt yhtään lukua.")