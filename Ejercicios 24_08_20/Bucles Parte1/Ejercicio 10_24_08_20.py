# 10- Tenemos 3 alumnos con notas de 3 materias. Necesitamos saber el promedio de cada materia y
# luego su promedio general. Si el resultado es mayor a 90 = A, 80= B, 70=C 60 =D. Definan el
# ejercicio en varias funciones para su mejor desarrollo. Al final imprimir los alumnos con su
# calificación de letra.

alumnos={}
for alumno in range(1):
    alumnos[f'Nombre']=input("Ingrese nombre del alumno: ")
    
    for materia in range(1):
        alumnos[f'Materia{materia}']=input("Ingrese materia del alumno: ")
        alumnos[f'Notas{materia}'] = []
        for nota in range(3):
            alumnos[f'Notas{materia}'].append(int(input("Ingrese Nota:")))
       
print(alumnos)
