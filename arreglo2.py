numero = int(input("Ingrese un numero : "))
lista_numero = [2,4,5,6,7,8,9]

for i  in lista_numero:
    lista_numero.count(numero)
if numero in lista_numero:
      print(f"El numero {numero} se encuentra dentro de la lista")  
else:
      print (f"El numero {numero} no se encuetra dentro de la lista")     