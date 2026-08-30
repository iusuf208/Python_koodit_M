luku = int(input("Anna kokonaisluku: "))

if luku < 2:
    on_alkuluku = False
else:
    on_alkuluku = True
    for jakaja in range(2, luku):
        if luku % jakaja == 0:
            on_alkuluku = False
            break

if on_alkuluku:
    print(f"Luku {luku} on alkuluku.")
else:
    print(f"Luku {luku} ei ole alkuluku.")