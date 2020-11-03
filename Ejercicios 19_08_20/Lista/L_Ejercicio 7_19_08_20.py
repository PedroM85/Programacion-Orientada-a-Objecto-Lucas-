# 7) tenemos la siguiente lista animales = ["oso hormiguero", "tejon", "pato", "emu", "zorro del desierto"].
# Debemos obtener el index de “pato” para luego insertar “cobra”.

animales = ["oso hormiguero", "tejon", "pato", "emu", "zorro del desierto"]


print(animales)

indice= animales.index("pato")
print("El indice de pato es ",animales.index("pato"))


animales.pop(indice)
print(animales)

animales.insert(indice,"cobra")
print(animales)