kaupungit = []

for i in range(5):
    nimi = input(f"Anna kaupungin nimi {i + 1}/5: ")
    kaupungit.append(nimi)

print("\nSyöttämäsi kaupungit:")

for kaupunki in kaupungit:
    print(kaupunki)
