"""De una lista de números, identifique el que más se repite."""

numeros = [3,2,5,3,3,4,8,4,8]
numeroR= 0
for i in range(len(numeros)): 
    cant = numeros.count(numeros[i])
    if i==0:
        numeroR= numeros[i]
        rep =  numeros.count(numeros[i])         
    else:
       if cant > rep:
        numeroR = numeros[i] 
       rep=numeros.count(numeros[i])
       
    
print(f"El numero {numeroR} es el que mas se repite")


             








 
     
 
    


   

   
 