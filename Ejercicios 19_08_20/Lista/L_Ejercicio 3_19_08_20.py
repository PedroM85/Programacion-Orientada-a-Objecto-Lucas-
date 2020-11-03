# 3)crear la siguiente lista animales = ["mono", "elefante", "tigre", "oso"], luego remplazar el tigre por un
# perro. Luego remplazar el oso por un gato.

animales = ["mono", "elefante", "tigre", "oso"]

print(animales)

animales.pop(2)
animales.insert(2,"perro")
print(animales)

animales.pop(3)
animales.insert(3,"gato")
print(animales)


