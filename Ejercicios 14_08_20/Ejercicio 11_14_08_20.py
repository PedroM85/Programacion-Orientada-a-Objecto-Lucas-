# 11) Elaborar un programa para mostrar en clase. Debe tener cierta complejidad para que lo podamos
# resolver entre todos. No se puede utilizar ejercicios anteriores.


x = int(input("Ingrese un número entero y positivo para calcular su factorial: "))
n = 0
z = x

while (n + 1) < z:
    # print(str(n))
    x = x * (n + 1)
#     print(str(x))
    n = n + 1
#     print(str(n))
if x == 0:
    print("El resultado de 0! es 1")
else:
    print("El resultado de " + str(z) + "! es " + str(x))