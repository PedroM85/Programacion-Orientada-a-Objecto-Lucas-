# 10) Elabora un algoritmo para leer 3 números enteros diferentes entre si, y determinar el número mayor
# de los tres.
Contador=1

print("Ingrese 3 numeros enteros diferentes entre si")
print("Ingreso un numero",Contador)
a=int(input())
Contador=Contador+1
print("Ingreso un numero",Contador)
b=int(input())
Contador=Contador+1
print("Ingreso un numero",Contador)
c=int(input())
Contador=Contador+1

if a>b and a>c:
    print("El mayor es",a)
elif b>a and b>c:
    print("El mayor es",b)
else:
    print("El mayor es",c)

