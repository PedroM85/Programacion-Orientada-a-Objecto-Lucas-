import sys
import os
#armo un diccionario con los sistemas operativos como clave y los comandos
#que borran las consola como valores
comandos = {"posix":"clear","nt":"cls"}
 
#diccionario con cada una de las posiciones posibles como clave y como valor
#un espacio en blanco que ubicará la marca de cada jugador cuando la elijan
#para colocar su ficha
 
posiciones_tablero={1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}
 
#dicionario con las fichas de los 2 jugadores, cada ficha tendrá un posición
#asociada, inician en cero los valores, a medida que vayan definiendo posiciones
#se irán almacenando en el correspondiente diccionario y clave-ficha
fichas_jugadores = {1:{1:0,2:0,3:0},2:{1:0,2:0,3:0}}
marcas_jugadores = {1:"X",2:"O"}
jugador_actual = 1
ficha_actual = 1
 
def PintarTablero():
    ##utilizo el diccionario con comandos y pasandole la clave que
    ##retorna os.name que nos dice el sistema operativo en el que estamosd
    os.system(comandos[os.name])
    for nro in range(1,10):
        sys.stdout.write("["+posiciones_tablero[nro]+"]")
         if nro %3==0:
           
               
    ##lineas para debug, para poder hacer un seguimiento de la evolución
    ##de los diccionarios
    print ("\n")
    print ("posiciones_tablero")
    print (posiciones_tablero)
    print ("fichas_jugadores")
    print (fichas_jugadores)
 
def Jugar(jugador_actual=0, ficha_actual=0):
    pos_jugada = input("Jugador %i: ingrese posicion para la ficha %i:" % (jugador_actual, ficha_actual))
    fichas_jugadores[jugador_actual][ficha_actual]=pos_jugada
    posiciones_tablero[pos_jugada]=marcas_jugadores[jugador_actual]
         
 
while True:
    PintarTablero()
    if (ficha_actual==0):
        ficha_actual=input("Jugador %i ingrese el número de ficha a mover:" % jugador_actual)
 
    Jugar(jugador_actual, ficha_actual)
    jugador_actual+=1
    if jugador_actual == 3 :
        jugador_actual = 1
        ficha_actual+=1
        if ficha_actual == 4:
            ficha_actual = 0