compra = ["uva", "platano", "mango" , "pera"]
def listado (lista):
    text = ""
    
    for i in range(len(lista)):
     if i==0 :
         text= text + lista[i]
        
     elif i<=len(lista) -2 :
         text = text  + " , "  + lista[i] 
        
     elif i==len(lista) -1 :
         text = text + " y " + lista[i]

    print(f"Tu lista tiene : {str(text)} ")  


listado(compra)       
      
            
  