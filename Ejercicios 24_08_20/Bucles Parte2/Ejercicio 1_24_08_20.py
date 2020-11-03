# Crear una lista de enteros, inicializarlos segun valores aleatorios en el rango
# 1..20 y computar la media de los valores, el valor mas alto y el mas bajo
# (utilizando listas). Utilizar las funciones para generacion de numeros
# aleatorios de Python

import random

lista = []
for i in range(20):
    lista.append(random.randint(i, 20))
media = sum(lista)/float(len(lista))
print("La lista es: " + str(lista))
print("La media de los valores de la lista es: "+str(media))
print("El maximo de los valores de la lista es: " + str(max(lista)))
print("El minimo de los valores de la lista es: " + str(min(lista)))