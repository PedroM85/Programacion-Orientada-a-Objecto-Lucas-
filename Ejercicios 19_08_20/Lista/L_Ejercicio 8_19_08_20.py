# 8) imprimir el doble de la siguiente lista. mi_lista = [1,9,3,8,5,7].

mi_lista=[1,9,3,8,5,7]
b=[2]
mi_doble=[]


for i in range(len(mi_lista)):
    for y in range(len(b)):
        mi_doble.append(mi_lista[i] * b[y])

print(mi_doble)

