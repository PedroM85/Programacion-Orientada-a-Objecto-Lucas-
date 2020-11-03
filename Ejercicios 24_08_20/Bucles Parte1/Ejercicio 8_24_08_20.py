# 8- Modificar una lista de números reales que representan las calificaciones de los alumnos de una
# clase, para sustituir los valores numéricos por sus calificaciones alfanuméricas (Suspenso <,
# Aprobado > 6)
lista=[4,5,2,7,1,9]
Calificacion = ""
for i in range(0, len(lista)):
    nota = lista[i]
    if nota < 0 or nota > 10:
        calificacion = "Error"
    else:
        if nota < 6:
            calificacion = "Suspenso"
        else:
            calificacion = "Aprobado"
    lista[i] = calificacion
print(lista) 