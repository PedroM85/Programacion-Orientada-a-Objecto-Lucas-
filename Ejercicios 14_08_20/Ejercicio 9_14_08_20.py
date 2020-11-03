# 9)Se tiene registrado la producción (unidades) logradas por un operario a lo largo de la semana ( lunes a
# sábado. Elabore un algoritmo que nos muestre o nos diga si el operario recibirá incentivos sabiendo que
# el promedio de producción mínima es de 100 unidades.

contador = 0
promedio = 0

while True:
        if contador == 0:
            dia= "Lunes"
            print("Ingrese la produccion del",dia)
            produ=int(input())
            contador = contador + 1   
            promedio = produ
        elif contador ==1:
            dia = "Martes"
            print("Ingrese la produccion del",dia)
            produ=int(input())
            promedio = promedio + produ
            contador = contador + 1
        elif contador ==2:
            dia = "Miercoles"
            print("Ingrese la produccion del",dia)
            produ=int(input())
            promedio = promedio + produ
            contador = contador + 1
        elif contador ==3:
            dia = "Jueves"
            print("Ingrese la produccion del",dia)
            produ=int(input())
            promedio = promedio + produ
            contador = contador + 1
        elif contador ==4:
            dia = "Viernes"
            print("Ingrese la produccion del",dia)
            produ=int(input())
            promedio = promedio + produ
            contador = contador + 1
        else:
            dia = "Sabado"
            print("Ingrese la produccion del",dia)
            produ=int(input())
            promedio = promedio + produ
            break

promedio1= promedio /6
if promedio1 >= 100:
    print("El operario esta recibiendo incentivos por producir mas de ",round(promedio1,2),"unidades")
else:
    print("El operario no esta recibiendo incentivos por producir menos de ",round(promedio1,2),"unidades")
