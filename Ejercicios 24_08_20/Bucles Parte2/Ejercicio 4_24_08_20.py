# 4- Crear un script que muestre el nombre de cada país y sus ciudades desde la variable $ceu
# con el siguiente formato:
# Las ciudades de Argentina son:
# ● Buenos Aires
# ● Córdoba
# ● Santa Fé
# Las ciudades de Brasil son:
# ● Brasilia
# ● Rio de Janeiro
# ● Sao Pablo
# Las ciudades de Alemania son:
# ● Munich
# ● Hamburgo
# ● Berlin
# Las ciudades de Francia son:
# ● Paris
# ● Lion
# ● Marsella
# Agregarle a cada país un dato extra además de sus ciudades llamado
# esAmericano . Este valor debe ser true o false.
# ● Hacer que la impresión anterior no muestre países que no sean Americanos.

ceu=[{"Pais":"Argentina","Ciudades":["Buenos Aires","Córdoba","Santa Fé"], "Americanos":True},    
{"Pais":"Brasil","Ciudades":["Brasilia","Rio de Janeiro","Sao Pablo"], "Americanos":True},
{"Pais":"Alemania","Ciudades":["Munich","Hamburgo","Berlin"], "Americanos":False},
{"Pais":"Francia","Ciudades":["Paris","Lion","Berlin"], "Americanos":False}]

for i in ceu:
    if i["Americanos"]==True:  
        for ciudad in i["Ciudades"]:
            print(ciudad) 