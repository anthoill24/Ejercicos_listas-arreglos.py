lista = [ 1,3,4,5,7,6,8,7,5,4,3,1]
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
       
   