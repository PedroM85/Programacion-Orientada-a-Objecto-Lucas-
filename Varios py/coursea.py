def suma_par(x):
    acu=0
    for x in range(x):
        if x%2==0:
            acu = acu + x
        
    return(print(acu))
        
      

suma_par(101)

def ciclo(x):
    s = 0
    for n in range(x):
        s += n
    
    return(print(s))

ciclo(10)

n = 10

while n <= 10:
    print("prueba")


def es_primo(numero):
    acu = 0
    resultado = True

   for divisor in range(2, numero):

       if (numero % divisor) == 0:
           acu += numero
           resultado = False
           print(acu)
           break

   return resultado

es_primo(13)

s = 0

for n in range(1, 10):

    if n % 2 == 0:

        break;

    s += n
print(s)

s = 0

for n in range(1, 10):

   if n % 2 == 0:

        continue;

    s += n
print(s)



s = 0

for n in range(1, 10):

   if n % 11 == 0:

         break;

   s += n

else:

    s += 10

s = 0

for n in range(1, 10):

   if n % 2 == 0:

        continue;

    s += n


s = 0

for n in range(1, 10):

   if n % 2 == 0:

         pass;

   s += n


s = 0

for n in range(1, 10):

    if n % 2 != 0:

      continue;

s += n

else:

    s += 5

print(s)

class SumaDos():
    def __init__(self, datos):

        self.datos = datos

        self.indice = 0

    def __iter__(self):

        return self

    def __next__(self):

        if self.indice == len(self.datos):

        raise StopIteration()

        elemento = self.datos[self.indice] + 2

        self.indice += 1

        return elemento

list(SumaDos([1,2,3,4,5]))

