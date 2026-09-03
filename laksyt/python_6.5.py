def karsi_parittomat(luvut):
    parilliset = []
    for luku in luvut:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset

alkuperainen_lista = [1,2,3,4,5,6,7,8,9,10,11,12]
karsittu_lista = karsi_parittomat(alkuperainen_lista)

print(f"Alkuperäinen lista: {alkuperainen_lista}")
print(f"Karsittu lista (vain parilliset): {karsittu_lista}")