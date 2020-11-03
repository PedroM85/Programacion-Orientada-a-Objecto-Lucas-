# 1) Tenemos residentes en una ciudad, hombres 4500, mujeres 5500 y niños 3000. Crear un
# diccionario con los datos brindados, para luego mostrar la cantidad de habitantes que hay entre
# mujeres y niños.

cuidad = {}

cuidad["Hombre"] = 4500
cuidad["Mujeres"] = 5500
cuidad["Niños"] = 3000

print(cuidad)


print(str(int(cuidad.get('Mujeres')) + int(cuidad.get('Niños')) )) 



