# 4) Realizar un inventario de los siguientes productos:
# - Harina: 500 unidades
# - Aceite: 800 unidades
# - Arroz: 400 unidades
# - Leche: 900 unidades
# - Agua: 2000 unidades

inventario = {"Harina":500,"Aceite": 800,"Arroz":400,"Leche":900,"Agua":2000}

#print(inventario)
# Luego, borrar 1000 unidades de agua y 200 de aceite.
# para el agua

for articulo in inventario.keys():
    if articulo == "Agua":
        inventario[articulo]  += 500
    if articulo == "Aceite":
        inventario[articulo]-=200
    if articulo == "Leche":
       inventario[articulo]+=200
    if articulo == "Harina":
        inventario[articulo]-=500

print(inventario)