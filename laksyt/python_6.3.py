def gallonat_l(gallonat):
    return gallonat * 3.785

while True:
    syote_gallonat = float(input("Anna gallonamäärä (negatiivinen luku lopettaa): "))

    if syote_gallonat < 0:
        print("Ohjelma lopetettu")
        break

    litrat = gallonat_l(syote_gallonat)
    print(f"{syote_gallonat} gallonaa on {litrat:.3f} litraa.\n")