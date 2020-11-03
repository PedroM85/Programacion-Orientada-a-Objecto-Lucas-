# 2- Tenemos el siguiente puntaje score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
# "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
# "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
# "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
# "x": 8, "z": 10}
# Tenemos que realizar una función que al poner una palabra nos diga cual es su puntaje.
# Ojo con poner mayúsculas y minúsculas, la función debe tomarlas igual.


def convertidor(score,palabra ):
    resultado=0
    text=palabra.lower()

    for i in text:
        resultado+=score[i]
    return resultado

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
"f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
"l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
"r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
"x": 8, "z": 10}


print("INTRODUZCA UN TEXTO")
text1=str.lower(input())

print(convertidor(score,text1))
