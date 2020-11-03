# 7- Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. Por
# último, muestra los números ordenados de menor a mayor.

lista = []
 
theend = False
 
while(not theend):
    numero = int(input("Introduzca un numero: "))
    if(numero == 0):
        theend=True
    else:
        lista.append(numero)
 
lista.sort() #ordena la lista
 
print(lista)