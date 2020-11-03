

import random 
import time
import os


def presentacion_1():



    print()
    print("           TRES EN RAYA")
    print()
    print()
    print("               1. Fácil")
    print("               2. Difícil")
    print()
    print()
    print()

    nivel = ""
    while nivel != "1" and nivel !="2":
        nivel = input("               ---> ")

    return int(nivel)


def presentacion_2():



    print()
    print("                 TRES EN RAYA ")
    print()
    print()
    print("                 Sale la Ficha O")
    print()
    print( "                Elige: O / X ")
    print()
    print()

    ficha = ""
    while ficha != "O" and ficha != "X":
        ficha = input("   ---> ").upper()

    if ficha == "O":
        humano = "O"
        ordenador = "X"
    else:
        humano = "X"
        ordenador = "O"

    return humano, ordenador


def mostrar_tablero(tablero):



    print()
    print("              TRES EN RAYA")
    print()
    print("      1         |2         |3")
    print("          {}     |    {}     |     {} ".format(tablero[0], tablero[1], tablero[2]))
    print("                |          |")
    print("      ----------+----------+------------")
    print("      4         |5         |6")
    print("          {}     |    {}     |     {} ".format(tablero[3], tablero[4], tablero[5]))
    print("                |          |")
    print("      ----------+----------+------------")
    print("      7         |8         |9")
    print("          {}     |    {}     |     {} ".format(tablero[6], tablero[7], tablero[8]))
    print("                |          |")
    print()


def seguir_jugando():


    
    print()
    respuesta= input("                ¿Otra partida (s)?").lower()
    if respuesta == "s" or respuesta == "si":
        return True
    else:
        return False


def hay_ganador(tablero, jugador):



    if tablero[0] == tablero[1] == tablero[2] == jugador or \
       tablero[3] == tablero[4] == tablero[5] == jugador or \
       tablero[6] == tablero[7] == tablero[8] == jugador or \
       tablero[0] == tablero[3] == tablero[6] == jugador or \
       tablero[1] == tablero[4] == tablero[7] == jugador or \
       tablero[2] == tablero[5] == tablero[8] == jugador or \
       tablero[0] == tablero[4] == tablero[8] == jugador or \
       tablero[2] == tablero[4] == tablero[6] == jugador:
       return True
    else:
       return False


def tablero_lleno(tablero):



    for i in tablero:
        
        if i == " ":
            return False

    return True


def casilla_libre(tablero, casilla):



    return tablero[casilla] == " "


def movimiento_jugador(tablero):



    posiciones = ["1","2","3","4","5","6","7","8","9"]
    posicion = None
    while True:
        if posicion not in posiciones:
            posicion = input("    Te toca(1-9): ")
        else:
            posicion = int(posicion)
            if not casilla_libre(tablero, posicion-1):
                print("    Esta posicion esta ocupada")
            else:
                return posicion-1


def mov_ordenador_facil(tablero, jugador):

    for i in range(9):
        copia = list(tablero)
        if casilla_libre(copia, i):
            copia[i]= jugador
            if hay_ganador(copia, jugador):
                return i
    
    while True:
        casilla = random.randint(0,8)
        if not casilla_libre(tablero, casilla):
            casilla= random.randint(0,8)
        else:
            return casilla
            
def mov_ordenador_dificil(tablero,maquina,usuario):

    for i in range(9):
        copia = list(tablero)
        if casilla_libre(copia, i):
            copia[i]= maquina
            if hay_ganador(copia, maquina):
                return i
    
    for i in range(9):
        copia = list(tablero)
        if casilla_libre(copia, i):
            copia[i]= usuario
            if hay_ganador(copia, usuario):
                return i
    
    if ordenador == "X":
        if tablero[4] == " ":
            return 4
        else:
            vacias = []
            for i in [0,2,6,8]:
                if tablero[i] == " ":
                    vacias.append(i)
                return random.choice(vacias)
    
    if ordenador == "O":
        contador = 0
        for i in range(9):
            if tablero[i] == " ":
                contador += 1
        if contador == 7:
            if tablero[4] == " ":
                return 4
    
    while  True:
        casilla = random.randint(0,8)
        if not casilla_libre(tablero, casilla):
            casilla = random.randint(0,8)
        else:
            return casilla













###########################################################################################3

jugando = True

while jugando:

    tablero = [" "] * 9

    os.system("cls")

    nivel = presentacion_1()

    os.system("cls")

    humano, ordenador = presentacion_2()

    os.system("cls")

    mostrar_tablero(tablero)

    if humano == "O":
        turno = "Humano"
    else:
        turno = "Ordenador"
    
    partida = True

    while partida:

        if tablero_lleno(tablero):
            print("            Empate")
            partida= False
        
        elif turno == "Humano":
            casilla = movimiento_jugador(tablero)
            tablero[casilla] = humano
            turno = "Ordenador"
            os.system("cls")
            mostrar_tablero(tablero)
            if hay_ganador(tablero, humano):
                print("           Has Ganado")
                partida = False
        
        elif turno == "Ordenador":
            print("     El ordenador esta pensando ...")
            time.sleep(2)
            if nivel == 1:
                casilla = mov_ordenador_facil(tablero, humano)
            elif nivel == 2:
                casilla = mov_ordenador_dificil(tablero, ordenador, humano)
            tablero[casilla] = ordenador
            turno = "Humano"
            os.system("cls")
            mostrar_tablero(tablero)
            if hay_ganador(tablero, ordenador):
                print("      Has perdido")
                partida = False
                
                
    jugando = seguir_jugando()       


    
    



    

