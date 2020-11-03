import random

jugador = True

lista=[1,2,3,4,5,6]

while jugador:

    sum=0

    a = random.choice(lista)
    b = random.choice(lista)

    sum = a + b

    print("El resultado de la primera lanzada es:" , a)
    print("El resultado de la segunda lanzada es:" , b)
    print("La suma de los dados es: " , sum)

    
    print()
    respuesta= input("                ¿Otra partida (s)?").lower()
    if respuesta == "s" or respuesta == "si":
        jugador = True
    else:
        jugador = False
