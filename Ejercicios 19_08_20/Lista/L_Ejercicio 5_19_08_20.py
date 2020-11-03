# 5) tenemos una valija con lo siguiente: valija = ["anteojos", "sombrero", "pasaporte", "computadora",
# "traje", "zapatos"]. Necesitamos separar lo que tenemos en primero, segundo y tercero. Imprimir los
# resultados de las separaciones. Queda en ustedes en que momento ponen cada elemento.

valija = ["anteojos", "sombrero", "pasaporte", "computadora","traje", "zapatos"]


documento = valija[:len(valija)//2]
valija = valija[len(valija)//2:]


print(documento)
print(valija)

