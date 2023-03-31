"""Dado un arreglo, indique si es simétrico, un arreglo es simétrico si
siendo longitud par los números de la primera mitad son iguales al
inverso de la otra mitad.
○ Ejemplo: El arreglo [1,2,3,3,2,1] es simétrico.
En caso de que la longitud sea impar, se ignorará el elemento central
y se seguirá la misma lógica anterior.
○ Ejemplo: El arreglo [3,5,7,8,7,5,3] es de longitud impar y es
simétrico."""

lista = [ 1,3,4,5,7,6,8,6,7,5,4,3,1]
longL = len(lista) 
resul= longL//2
print(resul%2)


for i in range(longL//2):
    if lista[i] != lista[longL-i-1]:
        mensaje= "No es simetrico"      
    elif resul % 2 != 0 and lista[i] == lista[longL-i-1]:

         mensaje= f"El arreglo {lista} es de longitud impar y es simetrico"
    else:
        mensaje= f"El arreglo{lista} es simetrico"     

print(mensaje)
       
   