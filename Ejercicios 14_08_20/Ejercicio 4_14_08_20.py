#4) Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor.

print("Escriba un numero entero:")
A1 = int(input())
print("Escriba un segundo numero entero:")
A2 = int(input())

if A1>A2:
    recidu=A1%A2
    if recidu ==0:
        print("El mayor es", A1, "y es multiplo de",A2)
    else:
        print("El mayor es", A1 ,"y no es multiplo de",A2)
elif A1<A2:    
    recidu=A2%A1
    if recidu ==0:
        print("El mayor es", A1, "y es multiplo de",A2)
    else:
        print("El mayor es", A1, "y no es multiplo de",A2)
else:
    print("los numeros son iguales")