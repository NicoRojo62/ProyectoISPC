# LABORATORIO
# 
# Tiempo Estimado
# 10-15 minutos
# 
# Nivel de Dificultad
# Fácil
# 
# Objetivos
# Familiarizar al estudiante con:
# 
# Crear y modificar listas simples.
# Utilizar métodos para modificar listas.
# Escenario
# Los Beatles fueron uno de los grupos de música más populares de la década de 1960 y la banda más vendida en la historia. Algunas personas los consideran el acto más influyente de la era del rock. De hecho, se incluyeron en la compilación de la revista Time de las 100 personas más influyentes del siglo XX.
# 
# a banda sufrió muchos cambios de formación, que culminaron en 1962 con la formación de John Lennon, Paul McCartney, George Harrison y Richard Starkey (mejor conocido como Ringo Starr).
# 
# 
# Escribe un programa que refleje estos cambios y le permita practicar con el concepto de listas. Tu tarea es:
# 
# Paso 1: Crea una lista vacía llamada beatles.
# Paso 2: Emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison.
# Paso 3: Emplea el buclefor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best.
# Paso 4: Usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista.
# Paso 5: Usa el método insert() para agregar a Ringo Starr al principio de la lista.
# Por cierto, ¿eres fan de los Beatles? (Los Beatles son una de las bandas favoritas de Greg. Pero espera...¿Quién es Greg?)
# 
# 

# paso 1
Beatles = []
print("Paso 1:", Beatles)

# paso 2

Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print(Beatles[1])
print("Paso 2:", Beatles)
# paso 3
for i in range(2):
    Beatles.append(input("Nombre: "))
print("Paso 3:", Beatles)

# paso 4
for i in range(2):
    del Beatles[len(Beatles)-1]
print("Paso 4:", Beatles)

# paso 5
Beatles.insert(0,"Ringo Starr")
print("Paso 5:", Beatles)

# probando la longitud de la lista
print("Los Fav", len(Beatles))