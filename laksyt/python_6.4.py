def laske_summa(lukulista):
    summa = 0
    for luku in lukulista:
        summa += luku
    return summa

testilista = [3,7,12,5,8]
tulos = laske_summa(testilista)

print(f"Listan {testilista} lukujen summa on:  {tulos}")