"""Dada un alista de números enteros, determine si esta tiene elementos duplicados. El programa debe decir:
La lista contiene elementos duplicados
o La lista no contiene elementos duplicados"""

# numeros = ["elefante", "pato", "ranas"]
numeros = [10,7,8,90]
for i in numeros:
    cant = numeros.count(i)
    if cant >=2:
        print("La lista contiene elementos duplicados")
        break
else:
    print("La lista no contiene elementos duplicados")            
