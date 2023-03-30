# numeros = ["elefante", "pato", "ranas"]
numeros = [10,7,8,90,9,100, 20, 100]
for i in numeros:
    cant = numeros.count(i)
    if cant >=2:
        print("La lista contiene elementos duplicados")
        break

else:
    print("La lista no contiene elementos duplicados")            
