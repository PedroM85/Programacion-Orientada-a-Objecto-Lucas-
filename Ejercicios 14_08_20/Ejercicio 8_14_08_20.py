# 8) Capturar las calificaciones obtenidas por un estudiante en tres exámenes parciales e imprimir su
# promedio final seguido del mensaje correspondiente de acuerdo a la siguiente tabla:

print("Ingresa 3 notas obtenidas:")
print("Nota 1")
n1=int(input())
print("Nota 2")
n2=int(input())
print("Nota 3")
n3=int(input())

nTotal=n1+n2+n3
promedio= nTotal/3

if promedio == 100:
    a="Excelente"
elif promedio >= 90:
    a="Muy bien"
elif promedio >= 80:
    a="Bien"
elif promedio >= 70:
    a="Regular"
elif promedio >= 60:
    a="Suficiente"
else:
    a="Reprobado"
print("Su promedio final es",round(promedio,2),",",a)
