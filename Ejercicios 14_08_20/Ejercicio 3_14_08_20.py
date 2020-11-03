# 3) Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han
# pasado desde ese año o cuántos años faltan para llegar a ese año.
print("Escriba el año actual:")
A1 = int(input())
print("Escriba el año Cualquiera:")
A2 = int(input())

if A1>A2:
    opera=A1-A2
    if opera ==1:
        print("Desde el año",A1,"Han pasado",opera,"año")
    else:
        print("Desde el año",A1,"Han pasado",opera,"años")
elif A1<A2:
    opera=A2-A1
    if opera ==1:
        print("Desde el año",A1,"Han pasado",opera,"año")
    else:
        print("Desde el año",A1,"Han pasado",opera,"años")
else:
    print("Los años son  iguales")