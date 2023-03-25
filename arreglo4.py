lista0 = [2,5,7]
lista1 = [2,5,8]
a = [3,4,5,2,43,9,6,13]
b = [3,4,5,2,45,7,8,10]

def diferencia(lista, lista2):
 suma= 0
 for i in range(len(lista)):
    conteo= lista.count(lista2[i])    
    if conteo == 0:
     suma += 1
 print(f"La diferencia entre ambos es de : {int(suma)}")

diferencia(lista0, lista1)
diferencia (a,b)
    
    
    


