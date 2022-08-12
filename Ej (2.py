DNI= 23546987
Nombre= "María"
Apellido= "Perez"
Número= 4789689
Dirección= "Pueyrredon 811"

Dueño2=[DNI, Nombre, Apellido, Número, Dirección]
for x in Dueño2:
    if x == DNI:
        Dueño2.remove(x)
    elif x == Apellido:
        Dueño2.remove(x)
print(Dueño2)
