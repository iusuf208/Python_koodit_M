leiviska = float(input("Anna leiviskä: "))
naula = float(input("Anna naula: "))
luoti = float(input("Anna luoti: "))

lei = 8500
nau = 425
luo = 13.3

gramma = (lei * leiviska + nau * naula + luo * luoti) % 1000

print(F"Massa nykymittojen mukaan: {((leiviska * lei) + (naula * nau) + (luoti * luo))/1000} kilogramma ja {gramma}")