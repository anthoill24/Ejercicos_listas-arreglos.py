"""Dada una lista de 10 números enteros, se requiere imprimir esos
números en orden inverso al que fueron ingresados."""

lista_de_numeros = [2,45,6,7,1,2,3,5, 9, 10]

def lista_inv(lista):
    lista.reverse()
    print(lista)

lista_inv(lista_de_numeros)    