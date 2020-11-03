# 1) Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si la división
# es exacta o no.

a=int(input("Introduzca numero 1 "))
b=int(input("Introduzca numero 2 "))
4
d=float(a / b)
e=a%b

print("El resultado es:", d)
if e > 0:
    print("La division no es exacta")
else:
    print("La division es exacta")