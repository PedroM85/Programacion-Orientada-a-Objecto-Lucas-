# 5- Emplear con diccionarios y array el ejercicio para obtener el promedio de nota de los alumnos
# del ejercicio 10 de bucles. Poner todas las notas y su nombre en una variable. Luego devolver un
# diccionario con el nombre de cada alumno y su promedio.

alumnos={}
for alumno in range(1):
    alumnos['nombre']=input("Ingrese nombre del alumno ")
    for materia in range(1):
        alumnos[f'Materia{materia}']=input("Ingrese materia del alumno ")
        alumnos[f'Notas{materia}']=[]
        for nota in range(2):
            alumnos[f'Notas{materia}'].append(int(input('Ingrese nota: ')))
            


print(alumnos)
print(nota)
print(len(nota[]))