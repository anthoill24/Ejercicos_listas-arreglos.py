"""Dada dos listas (lista1 y lista2), de como resultado dos listas
resultantes: una de la suma entre lista1 y lista2, y otra de la resta"""

numeros = [3,4,5,6,8]
numeros2 = [5,8,9,4,6]
resta = []
suma = []

for i in range(len(numeros)):
    suma.append(numeros[i] + numeros2[i])

    resta.append(numeros[i] - numeros2[i])

print(resta)
print(suma)



