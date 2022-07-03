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
# Indexación de listas.
# Utilizar operadoresin y not in.
# Escenario
# Imagina una lista: no muy larga ni muy complicada, solo una lista simple que contiene algunos números enteros. Algunos de estos números pueden estar repetidos, y esta es la clave. No queremos ninguna repetición. Queremos que sean eliminados.
# 
# Tu tarea es escribir un programa que elimine todas las repeticiones de números de la lista. El objetivo es tener una lista en la que todos los números aparezcan no más de una vez.
# 
# Nota: Asume que la lista original está ya dentro del código, no tienes que ingresarla desde el teclado. Por supuesto, puedes mejorar el código y agregar una parte que pueda llevar a cabo una conversación con el usuario y obtener todos los datos.
# 
# Sugerencia: Te recomendamos que crees una nueva lista como área de trabajo temporal, no necesitas actualizar la lista actual.
# 
# No hemos proporcionado datos de prueba, ya que sería demasiado fácil. Puedes usar nuestro esqueleto en su lugar.

# Este es un intento que por alguna razon da correcto con este ejemplo
# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# 
# print(len(my_list))
# for i in my_list:
#     for num in range(1,len(my_list)):
#         if i == num:
#             del(my_list[num])
#             break
#         print(my_list)
#     print(my_list)
# print("La lista con elementos únicos:")
# print(my_list)

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)
my_list = new_list[:]
print("La lista con elementos únicos:")
print(my_list)
