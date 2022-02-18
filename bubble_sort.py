import random
import time

def bubble_sort(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i] #troca elementos
numeros = [117,45,63,21,87,62,12,5,45,7,81,7]
aleatorio = random.sample(range(1,20),10)
lista = aleatorio
lista.sort(key=int, reverse=True)
print(lista)