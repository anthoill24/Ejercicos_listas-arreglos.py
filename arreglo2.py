"""Dado un arreglo de números (numbers) y un número entero n,
determine si n se encuentra en el arreglo. El programa debe imprimir
True o False como corresponda."""

numero = int(input("Ingrese un numero : "))
lista_numero = [2,4,5,6,7,8,9]

for i  in lista_numero:
 if numero in lista_numero:
      print(f"El numero {numero} se encuentra dentro de la lista")  
      break
else:
      print (f"El numero {numero} no se encuetra dentro de la lista")     