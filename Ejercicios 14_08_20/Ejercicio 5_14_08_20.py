#Escriba un PROGRAMA que pida tres números y que escriba si son los tres iguales,
#si hay dos iguales o si son los tres distintos
print("Escriba el primer numero: ")
n1=int(input())
print('Escriba el segundo numero: ')
n2=int(input())
print('Escriba el tercer numero: ')
n3=int(input())
if n1==n2==n3:
    print('Los tres numeros son iguales')
elif n1==n2 or n1==n3 or n2==n3:
    print('Hay dos numeros iguales')
else:
    print ('Los tres numeros son distintos')
    