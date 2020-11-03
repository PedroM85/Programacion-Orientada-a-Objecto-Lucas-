# 6) A un trabajador le pagan según sus horas y una tarifa de pago por horas. Si la cantidad de horas
# trabajadas es mayor a 40 horas. La tarifa se incrementa en un 50% para las horas extras. Calcular el
# salario del trabajador dadas las horas trabajadas y la tarifa.

print("Ingresa las horas trabajadas:")
horatra=int(input())
print("Ingresa la tarifa de pago:")
tarifa=int(input())

if horatra > 40:
    horas = horatra-40
    #print(horas)
    bono = horas*tarifa*1.50
    #print(bono)
    salariobase = 40 * tarifa
    #print(salariobase)
    Salariototal= salariobase+bono
    print("El salario base seria:", salariobase)
    print("El bono:",bono)
    print("El salario total:",Salariototal)
else:
    salariototal =(tarifa * horatra)
    print("El salario total:",salariototal)