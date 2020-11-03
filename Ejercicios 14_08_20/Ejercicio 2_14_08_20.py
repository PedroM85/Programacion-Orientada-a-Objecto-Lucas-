# 2) Escriba un programa que pida dos números y que conteste cuál es el menor y cuál el mayor o que
# escriba que son iguales.

a=int(input("Introduzca numero 1 "))
b=int(input("Introduzca numero 2 "))

if a > b:
    print(a," Es mayor que",b)
elif a < b:
    print (a," Es menor que",b)
else:
    print ("Los numeros sin iguales",a)
    
