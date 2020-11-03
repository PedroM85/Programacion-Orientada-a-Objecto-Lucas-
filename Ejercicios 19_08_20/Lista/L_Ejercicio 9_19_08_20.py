# 9) Tenemos la siguiente lista lista_inicial = [5, 3, 1, 2, 4]. Debemos realizar una lista_cuadrado y poner los
# numero de la lista_inicial elevados al cuadrado.


lista_inicial = [5, 3, 1, 2, 4]
lista_cuadrado = []

print("Lista Original",lista_inicial)

#for i in range(0,len(lista_inicial)):
#    lista_inicial[i]=lista_inicial[i]*lista_inicial[i]


#print("El cuadrado de la lista es", lista_inicial)

# 9.1


lista_cuadrado = [n**2 for n in lista_inicial]

print(lista_cuadrado)
