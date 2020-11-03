# 7) A un trabajador le descuentan de su sueldo el 10% si su sueldo es menor o igual a 1000. Por encima
# de 1000 y hasta 2000 el 5% del adicional, y por encima de 2000 el 3% del adicional. Calcular el descuento
# y sueldo neto que recibe el trabajador dado su sueldo.

print("Ingresa sueldo devengado:")
sueldo=int(input())

if sueldo <= 1000:
    descuento = sueldo * 0.1
    sueldo1 = sueldo - descuento
elif sueldo <= 2000:
    descuento = sueldo * 0.05
    sueldo1 = sueldo - descuento
else:
    descuento = sueldo * 0.03
    sueldo1 = sueldo - descuento
print("\n")
print("El descuento realizado es:",descuento)
print("El total del sueldo es:",sueldo1)