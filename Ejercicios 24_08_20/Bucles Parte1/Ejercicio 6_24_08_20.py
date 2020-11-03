# 6- Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena
# "estoy probando" debería devolver la cadena "odnaborp yotse"

cadena = "estoy probando"
invertida=""

cont = len(cadena)
indice = -1
while cont >= 1:
    invertida += cadena[indice]
    indice = indice + (-1)
    cont -= 1
print(invertida)