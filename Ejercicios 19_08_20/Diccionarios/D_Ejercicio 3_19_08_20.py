# 3) Definimos un diccionario con los barrios donde viven las siguientes personas:
# - Pedro: lugano
# - Ramiro: Boedo
# - Ricardo: Parque chas
# - Jazmín: Villa Urquiza
# - Andrea: San Cristóbal
# - Laura: Almagro
# Luego eliminar a Pedro y a Jazmín y agregar los siguientes:
# - Marcela: Boedo
# - Roberto: Agronomía

barrio = {}

barrio["Pedro"] = "lugano"
barrio["Ramiro"] = "Boedo"
barrio["Ricardo"] = "Parque chas"
barrio["Jazmin"] = "Villa Urquiza"
barrio["Andrea"] = "San Cristobal"
barrio["Laura"] = "Almagro"

print(barrio)

del barrio["Pedro"]
del barrio["Jazmin"]

print(barrio)

barrio["Marcela"] = "Boedo"
barrio["Roberto"] = "Agronomia"

print(barrio)