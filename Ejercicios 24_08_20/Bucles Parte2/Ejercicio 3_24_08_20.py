# 3- Partiendo de un archivo con la siguiente variable definida:
# $ceu =[{"Italia":"Roma", "Luxembourg":"Luxembourg", "Bélgica":"Bruselas",
# "Dinamarca":"Copenhagen",
# "Finlandia":"Helsinki", "Francia" :"Paris", "Slovakia":"Bratislava", "Eslovenia":"Ljubljana",
# "Alemania" : "Berlin",
# "Grecia" : "Athenas", "Irlanda":"Dublin", "Holanda":"Amsterdam",
# "Portugal":"Lisbon", "España":"Madrid", "Suecia":"Stockholm", "Reino Unido":"London",
# "Chipre":"Nicosia", "Lithuania":"Vilnius", "Republica Checa":"Prague",
# "Estonia":"Tallin", "Hungría":"Budapest", "Latvia":"Riga",
# "Malta":"Valletta", "Austria" : "Vienna", "Polonia":"Warsaw"}]
# Crear un script que muestre el nombre de la capital y el país desde la variable ceu.

ceu =[{"Italia":"Roma", "Luxembourg":"Luxembourg", "Bélgica":"Bruselas", "Dinamarca":"Copenhagen",
"Finlandia":"Helsinki", "Francia" :"Paris", "Slovakia":"Bratislava", "Eslovenia":"Ljubljana",
"Alemania" : "Berlin",  "Grecia" : "Athenas", "Irlanda":"Dublin", "Holanda":"Amsterdam",
"Portugal":"Lisbon", "España":"Madrid", "Suecia":"Stockholm", "Reino Unido":"London",
"Chipre":"Nicosia", "Lithuania":"Vilnius", "Republica Checa":"Prague",
"Estonia":"Tallin", "Hungría":"Budapest", "Latvia":"Riga",
"Malta":"Valletta", "Austria" : "Vienna", "Polonia":"Warsaw"}]

for i in ceu:
    for pais, capital in i.items():
        print(f"El pais es {pais} y su capital es {capital}")