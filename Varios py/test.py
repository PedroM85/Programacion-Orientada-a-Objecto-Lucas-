# import math


# with open("D:/Users/PedroM/Desktop/AntiLAG.txt","w") as a_file:
#     a_file.write(str(math.factorial(10)))

# with open ("D:/Users/PedroM/Desktop/coursea/AntiLAG3.txt","w") as a_file:
#     a_file.write("bana". 7.50)

# a_file = open("D:/Users/PedroM/Desktop/coursea/AntiLAG.txt","r")

# a_file.read()

# archivo creado
# archivo creado1
# archivo creado2
# archivo creado3

# import json

# json.dumps([1,2,3])

# json.loads('[1,2,3]')

# with open ("D:/Users/PedroM/Desktop/coursea/AntiLAG3.txt","w") as a_file:
#     json.dump([1,2,3], a_file)

# with open ("D:/Users/PedroM/Desktop/coursea/AntiLAG3.txt","r") as a_file:
#     a_list = json.load(a_file)

# import csv

# with open ("D:/Users/PedroM/Desktop/coursea/AntiLAG2.csv","r") as a_file:
#     reader = csv.reader(a_file, delimiter='||')
#     for row in reader:
#         print(", ".join(row))

# with open ("D:/Users/PedroM/Desktop/coursea/AntiLAG1.csv","a") as a_file:
#     writer = csv.writer(a_file, quoting=csv.QUOTE_NONE, quotechar='|',doublequote=False)
#     writer.writerow('Hola Mundo!')

# with open ("D:/Users/PedroM/Desktop/coursea/AntiLAG1.csv","a") as a_file:
#     writer = csv.writer(a_file, quoting=csv.QUOTE_NONE, quotechar='|',doublequote=False)
#     writer.writerow(['Hola Mundo!'])

# with open ("D:/Users/PedroM/Desktop/coursea/AntiLAG1.csv","a") as a_file:
#     writer = csv.writer(a_file, quoting=csv.QUOTE_NONE, quotechar='|',doublequote=False)
#     writer.writerow(["|Hola Mundo|"])

# with open ("D:/Users/PedroM/Desktop/coursea/AntiLAG1.csv","a") as a_file:
#     writer = csv.writer(a_file, quoting=csv.QUOTE_NONE, quotechar='|',doublequote=False)
#     writer.writerow(['Hola, Mundo!'])

# with open ("D:/Users/PedroM/Desktop/coursea/AntiLAG1.csv","a") as a_file:
#     writer = csv.writer(a_file, quoting=csv.QUOTE_NONE, quotechar='|',doublequote=False)
#     writer.writerow([""Hola, Mundo!""])


# with open ("D:/Users/PedroM/Desktop/coursea/AntiLAG1.csv","a") as a_file:
#     writer = csv.writer(a_file, quoting=csv.QUOTE_NONE, quotechar='|',doublequote=False)
#     writer.writerow( ['Pedro', 'Florencia', 'Matías', 'Jorge', 'María', 'Inés'])


# import csv
# reader = csv.reader(['Hola|, Mundo', 'Python'], escapechar='|')

# file_content = list(reader)

# print(file_content)

# cuadrados=[]
# for x in range(10):
#     cuadrados.append(x**2)

# a_list = [1, 3, 5, 7, 9]

# [x for x in range(10) if x %2 !=1]

a_list = [(6, 2), (1, 5), (2, 3), (4, 1), (5, 2), (1, 3)]

sorted(a_list, key=lambda  x: x[0]+x[1])

a_list.sort(key=lambda x: x[0]+x[1])

a_list = [7, 2, 3, 4, 5, 6, 1]

a_set = set('manzana')

subtotal=0
precios = {'manzana': 3.5, 'banana': 4.5, 'kiwi': 6.0, 'pera': 3.75, 'ciruela': 2.45, 'durazno': 4.55, 'melon': 7.35, 'sandia': 9.70, 'anana': 11.25}

for fruta, precio in precios.items():
    
    if fruta == 'manzana':
        subtotal= subtotal + (precio*2)
    if fruta == 'banana':
        subtotal = subtotal + (precio*2.5)
    if fruta == 'kiwi':
        subtotal = subtotal + (precio*1)
    if fruta == 'pera':
        subtotal = subtotal + (precio*3)
    if fruta == 'ciruela':
        subtotal = subtotal + (precio*1)
    if fruta == 'durazno':
        subtotal = subtotal + (precio*2)
    if fruta == 'melon':
        subtotal = subtotal + (precio*5)
    if fruta == 'sandia':
        subtotal = subtotal + (precio*10)
    if fruta == 'anana':
        subtotal = subtotal + (precio*3)
    print(f'El total de factura es', subtotal)


d={'a': 1, 'b': 2, 'c': 3, 'd':4, 'e':5}



def numeros_pares(n):

   return (x for x in range(n) if x % 2 == 0)