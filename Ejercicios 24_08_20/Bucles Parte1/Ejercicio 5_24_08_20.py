# 5- Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente
# todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y
# multip([1,2,3,4]) debería devolver 24.

sum1=[1,2,3,4]
multip=[1,2,3,4]

suma = 0
for i in sum1:
    suma += i
print(suma)

multipi = 1
for i in multip:
    multipi *= i
print(multipi) 
