numeros = [3,4,5,6,8]
numeros2 = [5,8,9,4,6]
resta = []
suma = []

for i in range(len(numeros)):
    suma.append(numeros[i] + numeros2[i])

    resta.append(numeros[i] - numeros2[i])

print(resta)
print(suma)



