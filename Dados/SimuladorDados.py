""" Simulador de dados, sirve para arrojar un resultado aleatorio
    de dos dados.
    author - Yonatan Henao R
    Version - 1.0.0

    Puntos a revisar:
    ¿Las formas como tu compañero generó los número aleatorios son correctas?
    R/ Validar la línea 15, 16 y 17 del archivo "Animar.py"

    ¿Tu compañero utiliza un ciclo while que consulta el valor de una variable?
    R/ Validar la línea 14 del archivo "Animar.py" o la línea 33 del archivo "SimuladorDados.py"

    ¿Antes de terminar el cuerpo del while, el programa pregunta al usuario si quiere tirar los dados nuevamente? 
    R/ Validar la línea 74 del archivo "SimuladorDados.py"

    Según la respuesta del usuario, ¿el programa actualiza el valor de la variable consultada en el while para que pueda terminar el programa si el usuario lo desea o seguir tirando los dados en caso que el usuario quiera eso?
    R/ Validar la línea 70 del archivo "SimuladorDados.py"


"""
from graficos import Animar
from graficos.presentacion import Encabezado
from contenido import Mensajes

Encabezado.autor()
Encabezado.banner()
Encabezado.dadosImg()

resultadoDadoUno = 0 
resultadoDadoDos = 0
salir = False

while(salir != True):
    Mensajes.menuPrincipal()
    Mensajes.ingreso()
    opcion = input()
    try:
        opcion = int(opcion)
        if opcion == 1:
            Animar.cargando()
            resultadoDadoUno = Animar.girarDado(1)
            print("El resultado del primer dado es: ", resultadoDadoUno, "\n\nPresione ENTER para continuar...")
            try:
                input()
            except ValueError as identifier:
                pass
            resultadoDadoDos = Animar.girarDado(1)
            print("El resultado del segundo dado es: ", resultadoDadoDos, "\n\nPresione ENTER para continuar...")
            try:
                input()
            except ValueError as identifier:
                pass
        else:
            if opcion == 2:
                Encabezado.autor()
                Encabezado.banner()
                Encabezado.dadosImg()
                Mensajes.resultados(resultadoDadoUno, resultadoDadoDos)
                print("\n\nPresione ENTER para continuar...")
                try:
                    input()
                except ValueError as identifier:
                    pass
            else:
                if opcion == 3:
                    Encabezado.autor()
                else:
                    if opcion == 4:
                        Animar.salir()
                        salir = True
                        # break
                    else:
                        Mensajes.opcionError()
        print("\nDeseas tirar los dados nuevamente?, ingresa la opción 1 para lanzar")
    except ValueError as identifier:
        Mensajes.ingresoError()
