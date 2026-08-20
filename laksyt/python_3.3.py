sukupuoli = input("Anna sukupuoli: ")
if sukupuoli == "nainen":
    hemoglobiiniarvo = float(input("Anna hemoglobiiniarvo: "))
    if hemoglobiiniarvo >= 117 and hemoglobiiniarvo <= 175:
        print("hemoglobiiniarvo on normaali")
    if hemoglobiiniarvo <= 116:
        print("hemoglobiiniarvo on alhainen")
    if hemoglobiiniarvo >= 176:
        print("hemoglobiiniarvo on korkea")
if sukupuoli == "mies":
    hemoglobiiniarvo = float(input("Anna hemoglobiiniarvo: "))
    if hemoglobiiniarvo >= 134 and hemoglobiiniarvo <= 195:
        print("hemoglobiiniarvo on normaali")
    if hemoglobiiniarvo <= 133:
        print("hemoglobiiniarvo on alhainen")
    if hemoglobiiniarvo >= 196:
        print("hemoglobiiniarvo on korkea")
