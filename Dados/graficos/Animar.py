# Módulo para animar un dado con caracteres ASCII
from os import system
import time
import random
from colorama import Fore, init
init()

def girarDado(n): # Módulo para animar el giro de un dado con caracteres ASCII
    system("cls")
    pasos = moverDado(n)
    cara_1 = 0
    cara_2 = 0
    cara_3 = 0
    while n <= 6:
        cara_1 = random.choice([1,2,3,4,5,6])
        cara_2 = random.choice([1,2,3,4,5,6])
        cara_3 = random.choice([1,2,3,4,5,6])
        if cara_1 != cara_2 and cara_1 != cara_3 and cara_2 != cara_3:
            print("\n\n\n\n\n", pasos +  Fore.YELLOW + "  ________")
            print(pasos + "  /\\       \\")
            print(pasos + " /  \\ " + Fore.GREEN,cara_1,Fore.YELLOW+"   \\")
            print(pasos + "{" + Fore.RED,cara_2,Fore.YELLOW+" }-------}")
            print(pasos +  Fore.YELLOW + " \\  /  " + Fore.BLUE,cara_3,Fore.YELLOW+"  /")
            print(pasos + "  \\/_______/")
            n+=1
            time.sleep(0.3)
            system("cls")
            print(pasos + Fore.YELLOW + "    ____ ________")
            print(pasos + "   |    |        |")
            print(pasos + "   |" + Fore.RED,cara_2,Fore.YELLOW + " |   " + Fore.GREEN,cara_1,Fore.YELLOW + "  |")
            print(pasos + "   |    |        |")
            print(pasos + "   |    |        |")
            print(pasos + "   ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
            time.sleep(0.3)
            girarDado(n)
            break
        else:
            girarDado(n)
            break
    # if n > 6:
    system("cls")
    print(Fore.YELLOW + "                                  ____ ________")
    print("                                 |    |        |")
    print("                                 |"+Fore.RED,cara_2,Fore.YELLOW + " |   " + Fore.GREEN,cara_1,Fore.YELLOW + "  |")
    print("                                 |    |        |")
    print("                                 |    |        |")
    print("                                 ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯" + Fore.RESET)
    return cara_1

def moverDado(paso): # Módulo para animar el movimiento horizontal de un dado con caracteres ASCII
    pasos=""
    for i in range(1, paso, 1):
        pasos += "      "
    return pasos

def cargando():
    for i in range(1, 7, 1):
        j = 1
        while j <= 4:
            system("cls")
            if j == 1:
                # system("cls")
                print("Cargando... -")
                time.sleep(0.1)
            else:
                if j == 2:
                    # system("cls")
                    print("Cargando... /")
                    time.sleep(0.1)
                else:
                    if j == 3:
                        print("Cargando... |")
                        time.sleep(0.1)
                    else:
                        # system("cls")
                        print("Cargando... \\")
                        time.sleep(0.1)
            j += 1

def salir():
    system("cls")
    print("a")
    time.sleep(1)
    system("cls")
    print("ad")
    time.sleep(1)
    system("cls")
    print("adi")
    time.sleep(1)
    system("cls")
    print("adio")
    time.sleep(1)
    system("cls")
    print("adios")
    time.sleep(1)
    system("cls")